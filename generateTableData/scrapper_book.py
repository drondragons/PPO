from math import ceil
from ebooklib import epub
from datetime import date
from random import randint
from bs4 import BeautifulSoup
from re import match, sub, search
from dataclasses import dataclass

from functions import Functions
from validation import Validator
from csv_handler import CSVHandler_dataclass
from generate_authors import AuthorsGenerator
from generate_publishers import PublishersGenerator
from scrapper import ScrapperCultureRU, replace_html_spaces, DEFAULT_HEADERS


DEFAULT_BOOKS_URL = 'https://www.culture.ru/literature/books'


class ScrapperBooks(ScrapperCultureRU):
    subdir = '?page={page}&limit=24&query=&sort=-views'
    epub_dir = '../TableData/BooksEpub'
    photo_dir = '../TableData/BooksPhoto'
    default_book_cover_photo = f'{photo_dir}/default_book_cover.png'
    default_book_cover_photo_url = 'https://i.pinimg.com/originals/a0/69/7a/a0697af2de64d67cf6dbb2a13dbc0457.png'
    

    def __init__(self, url=DEFAULT_BOOKS_URL, headers=DEFAULT_HEADERS):
        super().__init__(url, headers)


    def save_bytes_file(self, name, content):
        with open(name, 'wb') as f:
            f.write(content)
            
        
    def get_default_photo(self):
        response = self.session.get(self.default_book_cover_photo_url)
        self.save_bytes_file(self.default_book_cover_photo, response.content)
            
                
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
        return super().get_entity_attribute(soup, attr)[0]


    def get_annotation(self, soup):
        return super().get_entity_annotation(soup)


    def get_ebook_link(self, soup):
        ebook_link = str()
        links = soup.find_all('a', class_='about-entity_btn')
        for link in links:
            if link.text == 'Скачать книгу':
                ebook_link = link.get('href')
                break

        return ebook_link


    def save_ebook(self, url, title):
        index = 1
        title = title.replace(' ', '_')
        path = f'{self.epub_dir}/{title}_1.epub'
        while Functions.is_exist_file(path):
            index += 1
            path = f'{self.epub_dir}/{title}_{index}.epub'

        response = self.session.get(url)
        self.save_bytes_file(path, response.content)

        return path


    def get_pages(self, soup):
        poetry_page_symbols = 750
        symbols = prosa_page_symbols = 1500
        
        symbols_amount = len(soup.text)
        if soup.find(class_='block_poetry_out'):
            symbols = poetry_page_symbols

        return ceil(symbols_amount / symbols)


    def get_ebook_content(self, path, year):
        ebook = epub.read_epub(path)

        result = {'pages': 4, 'isbn': str(), 'publisher': str(),
                  'annotation': str(), 'publishing_year': 1500,
                  'writing_year': year, 'path': path}
        
        items = ebook.get_items()
        for item in items:
            if match(r'Text/chapter[0-9]+.xhtml', item.get_name()):
                soup = BeautifulSoup(item.get_content(),
                                     self.DEFAULT_PARSER)
                chapter = soup.find('body')

                result['pages'] += self.get_pages(chapter)

                generic_right = soup.find(class_='generic_right')

            if item.get_name() == 'Text/annotation.xhtml':
                soup_annotation = BeautifulSoup(item.get_content(),
                                                self.DEFAULT_PARSER)
                
                paragraphs = soup_annotation.find_all(class_='generic')
                for paragraph in paragraphs:
                    result['annotation'] += paragraph.text + '\\n' 
                result['annotation'] = replace_html_spaces(result['annotation'])
        
        if generic_right:
            year = sub('[^0-9]\-', '', generic_right.text).split('–')[-1]
            result['writing_year'] = int(year)

        generic_rights = soup_annotation.find_all(class_='generic_right')
        for generic_right in generic_rights:
            right = generic_right.text
            if 'ISBN' in right:
                result['isbn'] = right[search(r'\d', right).start():]
            else:
                result['publisher'] = right[right.find('«') + 1:right.find('»')]
                result['publishing_year'] = right[search(r'\d', right).start():]

        return result
        

    def get_ebook(self, soup, title, year):
        ebook_link = self.get_ebook_link(soup)
        
        path = self.save_ebook(ebook_link, title)

        return self.get_ebook_content(path, year)


    def get_tags(self, soup):
        tags = list()
        span = soup.find_all('span', class_='button_text')
        for el in span:
            if el.text != 'Литература':
                tags.append(el.text)

        return tags
    

    def get_book(self, url, index, authors, genres, publishers):
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
        author = self.get_author(about_entity)
        author = '{1} {0}'.format(*author.split(' '))
        print(author)
        author_index = 1
        for i, item in enumerate(authors):
            if author == item['initials']:
                author_index = i
                break

        print(index, authors[author_index])
        
        description = self.get_annotation(content)
        genre = set(self.get_genre(about_entity))
        ebook = self.get_ebook(about_entity, title,
                               authors[author_index]['death_date'])
        if (not isbn) and (isbn != ebook['isbn']):
            isbn = ebook['isbn']
        print(genre)
        print(tags)
        genre.update(tags)
        genre = list(genre)
        print(genre)
        genres.extend(item for item in genre if item not in genres)
        print(genres)
        genre_literary_work_record = list()
        for el in genre:
            for i, item in enumerate(genres, 1):
                if item == el:
                    genre_literary_work_record.append([index, i])
        print(genre_literary_work_record)
        '''
        print(f'\nisbn={isbn!r}\ntitle={title!r}\ngenre={genre!r}\n\
ebook={ebook!r}\nauthor={author!r}\n\
description={description!r}\n\n')
        '''
        
        author_literary_work_record = [index, author_index + 1]
        literary_work_record = [title, ebook['writing_year'], description,
                                ebook['path']]
        book_literary_work_recod = [index, index]
        
        #book_record = [title, isbn, ebook['pages'], randint(5, 15),
         #              ebook['publishing_year'], ]
        print(author_literary_work_record)
        print(literary_work_record)
        print(book_literary_work_recod)
        

    '''
    def get_authors(self):
        handler = CSVHandler_dataclass(AuthorsGenerator.file_path,
                                       AuthorsGenerator.class_type)
        
        authors = list()
        data = handler.get_csv_data()
        for index, author in enumerate(data, 1):
            item = {'initials': str(),
                    'death_date': date.today().year}
            item['initials'] = author.initials
            if author.death_date:
                item['death_date'] = int(author.death_date.split('.')[-1]) - 1
            authors.append(item)

        return authors
    

    def get_publishers(self):
        handler = CSVHandler_dataclass(PublishersGenerator.file_path,
                                       PublishersGenerator.class_type)
        publishers = handler.get_csv_data()
    '''    
        

    def get_books(self):
        if not Functions.is_exist_file(self.epub_dir):
            Functions.create_dir(self.epub_dir)
            
        if not Functions.is_exist_file(self.photo_dir):
            Functions.create_dir(self.photo_dir)

        if not Functions.is_exist_file(self.default_book_cover_photo):
            self.get_default_photo()

        authors = self.get_authors()
        publishers = self.get_publishers()
        
        books = list()
        genres = list()
        literary_works = list()
        urls = super().get_entities_urls(self.subdir)
        print(len(urls))
        urls = ['https://www.culture.ru/books/965/beseda-pyanogo-s-trezvym-chertom',
                'https://www.culture.ru/books/242/gore-ot-uma',
                'https://www.culture.ru/books/178/evgenii-onegin']
        for index, url in enumerate(urls, 1):
            self.get_book(url, index, authors, genres)
            input()
