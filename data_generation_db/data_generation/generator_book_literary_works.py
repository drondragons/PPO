import random
from dt_book import Book
from generator_books import BooksGenerator
from generator_genres import GenresGenerator
from generator_abstract import DataGenerator
from generator_authors import AuthorsGenerator
from dt_book_literary_work import BookLiteraryWork
from generator_publishers import PublishersGenerator
from csv_handler_dataclass import CSVHandler_dataclass
from generator_literary_works import LiteraryWorksGenerator
from generator_literary_work_genres import LiteraryWorkGenresGenerator
from generator_author_literary_work import AuthorLiteraryWorksGenerator


class BookLiteraryWorksGenerator(DataGenerator):
    def __init__(self, path='../TableData/BookLiteraryWorks.csv', class_type=BookLiteraryWork):
        super().__init__(path, class_type)
               
               
    def count_literary_works_by_attribute(self, container, attribute):
        d = dict()
        for record in container:
            tmp = getattr(record, attribute)
            d.setdefault(tmp, 0)
            d[tmp] += 1
        return d
    
    
    def find_entities_with_some_literary_works_index(self, d, limit):
        return [key for key, value in d.items() if value > limit]
    
    
    def find_entities_for_collection(self, indexes, container, attribute):
        return [getattr(container[index-1], attribute) for index in indexes]
    
    
    def find_entity_records(self, value, container, attribute):
        return [record for record in container if value in record[attribute]]
    
    
    def find_entities_records(self, entities, container, attribute):
        d = dict.fromkeys(entities, list())
        for entity in entities:
            d[entity] = self.find_entity_records(entity, container, attribute)
        return d   
        
        
    def find_entity_records_for_collection(self, literary_works):
        collection = list()
        collection_pages = 0
        limit_collection_pages = 600
        limit_literary_work_pages = 300
        print(len(literary_works))
        for literary_work in literary_works:
            if collection_pages >= limit_collection_pages:
                break
            
            pages = int(literary_work['pages'])
            print(pages, literary_work)
            if pages < limit_literary_work_pages:
                collection_pages += pages
                collection.append(literary_work)
        print(collection_pages, collection)
        print()
        print()
        input()
        return collection_pages, collection            
    
    
    def find_entities_records_for_collection(self, records):
        collections = dict.fromkeys(records.keys(), list())
        for key, value in records.items():
            print(key, len(value), value)
            input('privetqaz')
            collections[key] = self.find_entity_records_for_collection(value)
        return collections
            
            
    def generate_book_literary_work(self, index):
        return BookLiteraryWork(book_id=index, 
                                literary_work_id=index)

    
    def generate_title(self, title):
        collection_name = random.choice(['Сборник произведений', 'Избранное'])
        return f'{title}. {collection_name}' 
    
    
    def generate_publisher_id(self):
        handler = CSVHandler_dataclass(PublishersGenerator().path, PublishersGenerator().class_type)
        publishers = handler.get_csv_data()
        
        publisher = random.choice(publishers)
        return BooksGenerator().find_publisher_id(publisher.name, publishers)[0]
    
    
    def generate_annotation(self, records, title):
        names = ', '.join([record['title'] for record in records])
        return f'Аннотация к сборнику «{title}» по умолчанию.\\nКнига содержит следующие произведения: {names}.'
 
 
    def generate_book(self, data):
        print(data)
        input("data")
        pages = data[1][0]
        attribute = data[0]
        record = data[1][1]
        title = self.generate_title(attribute)
        return Book(title=title,
                    isbn=BooksGenerator().generate_isbn(str()),
                    total_pages=pages,
                    amount=BooksGenerator().generate_amount(),
                    publishing_year=BooksGenerator().generate_publishing_year(int()),
                    publisher_id=self.generate_publisher_id(),
                    price=BooksGenerator().generate_price(),
                    annotation=self.generate_annotation(record, title),
                    cover_path=record[0]['cover_path'],
                    library_location=BooksGenerator().generate_library_location())
    
    
    def find_literary_work_index(self, record):
        handler = CSVHandler_dataclass(LiteraryWorksGenerator().path, LiteraryWorksGenerator().class_type)
        literary_works = handler.get_csv_data()
        
        return [index for index, literary_work in enumerate(literary_works, 1) if record['title'] == literary_work.title][0]
        
            
    def generate_collection(self, collection):
        book = self.generate_book(collection)
        print(book)
        input("book")
        
        handler = CSVHandler_dataclass(BooksGenerator().path, BooksGenerator().class_type)
        handler.add_data_in_csv([book])
        books = handler.get_csv_data()
        
        result = list()
        for record in collection[1][1]:
            index = self.find_literary_work_index(record)
            result.append(BookLiteraryWork(book_id=len(books),
                                           literary_work_id=index))
        
        return result
    
            
    def generate_collections(self, collections):
        result = list()
        for collection in collections.items():
            result.extend(self.generate_collection(collection))
        return result
            

    def generate_collection_by_author(self, container):
        handler = CSVHandler_dataclass(AuthorLiteraryWorksGenerator().path, AuthorLiteraryWorksGenerator().class_type)
        author_literary_works = handler.get_csv_data()
        
        handler = CSVHandler_dataclass(AuthorsGenerator().path, AuthorsGenerator().class_type)
        authors = handler.get_csv_data()
        
        d = self.count_literary_works_by_attribute(author_literary_works, 'author_id')
        print(d)
        input()
        
        limit = 3
        authors_index = self.find_entities_with_some_literary_works_index(d, limit)
        print(authors_index)
        input()
        authors_for_collection = self.find_entities_for_collection(authors_index, authors, 'initials')
        print(authors_for_collection)
        input()
        authors_records = self.find_entities_records(authors_for_collection, container, 'author')
        print(authors_records)
        input()
        authors_collections = self.find_entities_records_for_collection(authors_records)
        print(authors_collections)
        input("TUTUTUTUTUTUTT")
        return self.generate_collections(authors_collections)
     
     
    def generate_collection_by_genre(self, container):
        handler = CSVHandler_dataclass(LiteraryWorkGenresGenerator().path, LiteraryWorkGenresGenerator().class_type)
        literary_work_genres = handler.get_csv_data()
        
        handler = CSVHandler_dataclass(GenresGenerator().path, GenresGenerator().class_type)
        genres = handler.get_csv_data()
        
        d = self.count_literary_works_by_attribute(literary_work_genres, 'genre_id')
        print(d)
        
        limit = 3
        genres_index = self.find_entities_with_some_literary_works_index(d, limit)
        print(genres_index)
        genres_for_collection = self.find_entities_for_collection(genres_index, genres, 'title')
        print(genres_for_collection)
        genres_records = self.find_entities_records(genres_for_collection, container, 'genre')
        print(genres_records)
        
        genres_collections = self.find_entities_records_for_collection(genres_records)
        print(genres_collections)
        return self.generate_collections(genres_collections) 
     

    def generate_book_literary_works(self, container):
        result = list()
        result.extend([self.generate_book_literary_work(i) for i, _ in enumerate(container, 1)])
        print(result)
        print()
        input()
        result.extend(self.generate_collection_by_author(container))
        print(result)
        print()
        input()
        result.extend(self.generate_collection_by_genre(container))
        print(result)
        print()
        return result
    

    def generate(self, container=list()):
        self.container = self.generate_book_literary_works(container)