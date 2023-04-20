from dateparser import parse
from bs4 import BeautifulSoup
from functions import Functions
from scrapper import ScrapperCultureRU, DEFAULT_HEADERS


DEFAULT_AUTHORS_URL = 'https://www.culture.ru/literature/persons'


class ScrapperAuthors(ScrapperCultureRU):
    subdir = '?rubricPath=&page={page}&limit=24&sort=-views'
    authors_photo_dir = '../TableData/AuthorsPhoto'
    
    
    def __init__(self, url=DEFAULT_AUTHORS_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)


    def get_initials(self, soup):
        initials = super().get_entity_header(soup)
        if initials.find(' (') != -1:
            initials = initials[:initials.find(' (')]
        
        return Functions.swap_name_surname(initials)
    

    def get_date(self, soup):
        birth_date = death_date = None

        dictionary = {'Годы жизни: ': None,
                      'Родился: ': None,
                      'Родилась: ': None}
        for key in dictionary:
            dictionary[key] = super().get_entity_attribute(soup, key)
            if dictionary[key]:
                value = dictionary[key][0]
                
                age = value.find(' (')
                delim = value.find('—') - 1
                end = delim if delim > age else age
                birth_date = parse(value[:end]).strftime('%d.%m.%Y')

                if delim == end:
                    death_date = parse(value[delim+3:]).strftime('%d.%m.%Y')
        
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
        authors = list()
        urls = super().get_entities_urls(self.subdir)
        for url in urls:
            author = self.get_author(url)
            authors.append(author)
        
        return authors
