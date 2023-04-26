import dateparser
from bs4 import BeautifulSoup
from functions import Functions
from scrapper import ScrapperCultureRU, DEFAULT_HEADERS


DEFAULT_AUTHORS_URL = 'https://www.culture.ru/literature/persons'


class ScrapperAuthors(ScrapperCultureRU):
    subdir = '?rubricPath=&page={page}&limit=24&sort=-views'
    
    photo_dir = '../TableData/AuthorsPhoto'
    
    default_author_photo = f'{photo_dir}/default_author_photo.jpg'
    default_author_photo_url = 'https://media.istockphoto.com/id/1087531642/ru/%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F/%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%BE%D0%B9-%D1%81%D0%B8%D0%BB%D1%83%D1%8D%D1%82-%D0%BB%D0%B8%D1%86%D0%B0-%D0%B8%D0%BB%D0%B8-%D0%B7%D0%BD%D0%B0%D1%87%D0%BE%D0%BA-%D0%BF%D1%80%D0%BE%D1%84%D0%B8%D0%BB%D1%8C-%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA%D0%B0-%D0%B0%D0%B2%D0%B0%D1%82%D0%B0%D1%80%D0%B0-%D0%BD%D0%B5%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D0%B9-%D0%B8%D0%BB%D0%B8-%D0%B0%D0%BD%D0%BE%D0%BD%D0%B8%D0%BC%D0%BD%D1%8B%D0%B9-%D1%87%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA.jpg?s=612x612&w=0&k=20&c=uabxlpVHOU_mwfEbQPCzZ_SU52Ly1xgUntQ9qyFELOc='
    
    
    def __init__(self, url=DEFAULT_AUTHORS_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)


    def get_default_photo(self):
        response = self.session.get(self.default_author_photo_url)
        Functions.save_bytes_file(self.default_author_photo, response.content)


    def get_initials(self, soup):
        initials = super().get_entity_header(soup)
        if initials.count('('):
            initials = initials[:initials.find(' (')]
        return Functions.swap_name_surname(initials)
    

    def get_date(self, soup):
        birth_date = death_date = None

        date_value = str()
        date_labels = ['Годы жизни: ', 'Родился: ', 'Родилась: ']
        for date_label in date_labels:
            date_value = super().get_entity_attribute(soup, date_label)
            if date_value:
                break
        
        date_value = date_value[0]
        
        age = date_value.find(' (')
        delim = date_value.find('-') - 1
        end = delim if delim > age else age
        
        birth_date = dateparser.parse(date_value[:end]).strftime('%d.%m.%Y')
        if delim == end:
            death_date = dateparser.parse(date_value[delim+3:]).strftime('%d.%m.%Y')
        
        return birth_date, death_date
        

    def get_photo_path(self, soup, name):
        name = name.replace(' ', '_')
        src = f'{self.authors_photo_dir}/{name}' + '_{index}.png'
        path = Functions.get_unused_path(src)
        
        url = soup.find('img')['src']
        photo = self.session.get(url).content
        Functions.save_bytes_file(path, photo)

        return path


    def get_biography(self, soup):
        return super().get_entity_annotation(soup)


    def get_author(self, url):
        print(url)
        response = self.session.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
        soup = soup.find('article', class_='article')
        soup = soup.find('div', class_='container_inner')

        initials = self.get_initials(soup)
        biography = self.get_biography(soup)
        birth_date, death_date = self.get_date(soup)
        photo_path = self.get_photo_path(soup, initials)
        
        return {'initials': initials,
                'birth_date': birth_date,
                'death_date': death_date,
                'photo_path': photo_path,
                'biography': biography}
        
            
    def get_authors(self):
        self.get_default_photo()
        print('\nСкачана фотография автора по умолчанию.\n')
        
        authors = list()
        print(f'\nПолучение данных о писателях с сайта {self.baseurl!r}.\n')
        urls = super().get_entities_urls(self.subdir)
        for url in urls:
            author = self.get_author(url)
            authors.append(author)
        print(f'\nПолучение данных о писателях с сайта {self.baseurl!r} завершено.\n')
        return authors

        
    def get_data(self):
        return self.get_authors()