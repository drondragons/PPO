import re
import math
import datetime
from ebooklib import epub
from bs4 import BeautifulSoup
from functions import Functions
from scrapper import ScrapperCultureRU, DEFAULT_HEADERS


DEFAULT_BOOKS_URL = 'https://www.culture.ru/literature/books'


class ScrapperLiterature(ScrapperCultureRU):
    subdir = '?page={page}&limit=24&query=&sort=-views'
    
    epub_dir = '../TableData/BooksEpub'
    photo_dir = '../TableData/BooksPhoto'

    default_book_cover_photo = f'{photo_dir}/default_book_cover.png'
    default_book_cover_photo_url = 'https://i.pinimg.com/originals/a0/69/7a/a0697af2de64d67cf6dbb2a13dbc0457.png'
    

    def __init__(self, url=DEFAULT_BOOKS_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)
            
        
    def get_default_photo(self):
        response = self.session.get(self.default_book_cover_photo_url)
        Functions.save_bytes_file(self.default_book_cover_photo, response.content)
            
                
    def get_title(self, soup):
        return super().get_entity_header(soup)


    def get_genre(self, soup):
        attr = 'Жанр: '
        return super().get_entity_attribute(soup, attr)


    def get_isbn(self, soup):
        attr = 'Международный стандартный книжный номер: '
        return super().get_entity_attribute(soup, attr)
    

    def get_author(self, soup):
        attr = 'Авторы: '
        author = super().get_entity_attribute(soup, attr)[0]
        return Functions.swap_name_surname(author)


    def get_annotation(self, soup, title):
        return super().get_entity_annotation(soup) if soup else f'Аннотация к произведению «{title}» по умолчанию.'


    def get_ebook_link(self, soup):
        links = soup.find_all('a', class_='about-entity_btn')
        ebook_link = [link.get('href') for link in links if link.text == 'Скачать книгу']
        return ebook_link[0]


    def save_ebook(self, url, title):
        title = title.replace(' ', '_')
        title = re.sub('[^а-яА-Яa-zA-Z0-9\_]', '', title)
        src = f'{self.epub_dir}/{title}' + '_{index}.epub'
        path = Functions.get_unused_path(src)
        
        response = self.session.get(url)
        Functions.save_bytes_file(path, response.content)

        return path


    def get_pages(self, soup):
        symbols = 1500
        poetry_page_symbols = 750
        
        symbols_amount = len(soup.text)
        if soup.find(class_='block_poetry_out'):
            symbols = poetry_page_symbols

        return math.ceil(symbols_amount / symbols)


    def get_ebook_content(self, path):
        ebook = epub.read_epub(path)

        result = {'pages': 4,
                  'path': path,
                  'isbn': None,
                  'publisher': None,
                  'annotation': str(),
                  'writing_year': None,
                  'publishing_year': None}
        
        items = ebook.get_items()
        for item in items:
            if re.match(r'Text/chapter[0-9]+.xhtml', item.get_name()):
                soup = BeautifulSoup(item.get_content(),
                                     self.DEFAULT_PARSER)
                chapter = soup.find('body')
                result['pages'] += self.get_pages(chapter)
                generic_right = soup.find(class_='generic_right')

            if item.get_name() == 'Text/annotation.xhtml':
                soup_annotation = BeautifulSoup(item.get_content(),
                                                self.DEFAULT_PARSER)
                
                paragraphs = soup_annotation.find_all(class_='generic')
                result['annotation'] = super().get_paragraphs(paragraphs)
        
        if generic_right:
            year = re.sub('[^0-9\–]', '', generic_right.text).split('–')[-1]
            result['writing_year'] = int(year) if year and int(year) < datetime.date.today().year else None

        generic_rights = soup_annotation.find_all(class_='generic_right')
        for generic_right in generic_rights:
            right = generic_right.text
            if 'ISBN' in right:
                result['isbn'] = right[re.search(r'\d', right).start():]
            else:
                result['publisher'] = right[right.find('«') + 1:right.find('»')]
                result['publishing_year'] = int(right[re.search(r'\d', right).start():])
        
        return result
        

    def get_ebook(self, soup, title):
        ebook_link = self.get_ebook_link(soup)
        
        path = self.save_ebook(ebook_link, title)

        return self.get_ebook_content(path)


    def get_tags(self, soup):
        soup = soup.find_all('span', class_='button_text')
        return [tag.text for tag in soup if tag.text != 'Литература']
    

    def get_record(self, url):
        print(url)
        response = self.session.get(url)
        print(response.status_code)
        soup = BeautifulSoup(response.text, self.DEFAULT_PARSER)
        soup = soup.find('article', class_='article')
        soup = soup.find('div', class_='container_inner')

        aside = soup.find('aside')
        content = soup.find('div', class_='styled-content')
        about_entity = soup.find('div', class_='about-entity')

        tags = set(self.get_tags(aside))
        isbn = self.get_isbn(about_entity)
        title = self.get_title(about_entity)
        description = self.get_annotation(content, title)
        genre = set(self.get_genre(about_entity))
        ebook = self.get_ebook(about_entity, title)
        author = self.get_author(about_entity)

        isbn = ebook['isbn'] if isbn != ebook['isbn'] else isbn

        genre.update(tags)
        genre = list(genre)

        return {'isbn': isbn,
                'title': title,
                'genre': genre,
                'author': author,
                'path': ebook['path'],
                'pages': ebook['pages'],
                'description': description,
                'publisher': ebook['publisher'],
                'annotation': ebook['annotation'],
                'writing_year': ebook['writing_year'],
                'publishing_year': ebook['publishing_year'],
                'cover_path': self.default_book_cover_photo}
        

    def get_literature(self):
        self.get_default_photo()
        print('\nСкачана книжная обложка по умолчанию.\n')
        
        books = list()
        print(f'\nПолучение данных о литературе с сайта {self.baseurl!r}.\n')
        urls = super().get_entities_urls(self.subdir)
        for url in urls:
            book = self.get_record(url)
            books.append(book)
        print(f'\nПолучение данных о литературе с сайта {self.baseurl!r} завершено.\n')
        return books


    def get_data(self):
        return self.get_literature()