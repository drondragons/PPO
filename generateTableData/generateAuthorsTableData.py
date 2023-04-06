from typing import Union
from dateparser import parse
from bs4 import BeautifulSoup
from dataclasses import dataclass

from AttributeValidator import Validator
from scrapper import ScrapperCultureRU, DEFAULT_HEADERS


DEFAULT_AUTHORS_URL = 'https://www.culture.ru/literature/persons'


@dataclass(frozen=True)
class Author:
    initials: str = Validator(str, [Validator.exist_validator,
                                    Validator.match_validator,
                                    Validator.length_validator],
                              1, 50, "^[а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+$")
    birth_date: str = Validator(str, [Validator.exist_validator,
                                      Validator.symbols_validator,
                                      Validator.length_validator],
                                5, 10, "[^\d\.]")
    death_date: Union[str, None] = None
    photo_path: str = Validator(str, [Validator.exist_validator,
                                      Validator.match_validator],
                                regex="^\.\.\/TableData\/AuthorsPhoto\/[а-яА-ЯёЁ\-\_]+\.png$")
    biography: str = Validator(str, [Validator.exist_validator])


class ScrapperAuthors(ScrapperCultureRU):
    subdir = '?rubricPath=&page={page}&limit=24&sort=-views'
    authors_photo_dir = '../TableData/AuthorsPhoto'
    
    
    def __init__(self, url=DEFAULT_AUTHORS_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)


    def get_author_initials(self, soup):
        return super().get_entity_header(soup)
    

    def get_author_date(self, soup):
        birth_date = None
        death_date = None

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
        

    def get_author_photo_path(self, soup, name):
        name = name.replace(' ', '_')
        url = soup.find('img')['src']
        
        photo = self.session.get(url).content
        path = f'{self.authors_photo_dir}/{name}.png'
        with open(path, 'wb') as f:
            f.write(photo)

        return path


    def get_author_biography(self, soup):
        return super().get_entity_annotation(soup)


    def get_author(self, url):
        print(url)
        response = self.session.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
        soup = soup.find('article', class_='article')
        soup = soup.find('div', class_='container_inner')

        initials = self.get_author_initials(soup)
        biography = self.get_author_biography(soup)
        birth_date, death_date = self.get_author_date(soup)
        photo_path = self.get_author_photo_path(soup, initials)
        
        return Author(initials=initials, birth_date=birth_date,
                      death_date=death_date, photo_path=photo_path,
                      biography=biography)
        
            
    def get_authors(self):
        authors = list()
        urls = super().get_entities_urls(self.subdir)
        for url in urls:
            author = self.get_author(url)
            authors.append(author)

        return authors
    

class AuthorsGenerator:
    class_type = Author
    file_path = "../TableData/Authors.csv"


    def __init__(self):
        self.container = list()


    def generate(self):
        scrapper = ScrapperAuthors()
        self.container = scrapper.get_authors()
