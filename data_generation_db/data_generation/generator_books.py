import random
import datetime
from faker import Faker

from dt_book import Book
from generator_abstract import DataGenerator
from generator_publishers import PublishersGenerator

from csv_handler_dataclass import CSVHandler_dataclass


class BooksGenerator(DataGenerator):
    def __init__(self, path='../TableData/Books.csv', class_type=Book):
        super().__init__(path, class_type)


    def generate_amount(self):
        return random.randint(5, 20)


    def generate_price(self):
        return random.randint(500, 2000)


    def generate_publishing_year(self, year):
        return int(year) if year else datetime.date.today().year - 1


    def generate_library_location(self):
        room_number = random.choice(['В первом', 'Во втором', 'В третьем', 'В четвёртом', 'В пятом'])
        bookcase_number = random.choice(['в первом', 'во втором', 'в третьем', 'в четвёртом'])
        return f'{room_number} зале,{bookcase_number} шкафу'


    def get_fake_isbn13(self):
        return Faker('ru_RU').isbn13()


    def generate_isbn(self, isbn):
        return isbn if isbn else self.get_fake_isbn13()
    

    def find_publisher_id(self, publisher, publishers):
        return [i for i, item in enumerate(publishers, 1) if item.name == publisher]
    

    def generate_publisher_id(self, publisher):
        handler = CSVHandler_dataclass(PublishersGenerator().path, PublishersGenerator().class_type)
        publishers = handler.get_csv_data()

        if not publisher:
            publisher = random.choice(publishers).name
            
        index = self.find_publisher_id(publisher, publishers)
        if not index:
            country_id = publishers[0].country_id
            item = PublishersGenerator().class_type(name=publisher, country_id=country_id)
            
            publishers.append(item)
            publishers.sort()
            handler.write_csv(publishers)
            index = self.find_publisher_id(publisher, publishers)

        return index[0]
    
    
    def generate_pages(self, pages):
        return int(pages)
    
                
    def generate_book(self, item):
        return Book(title=item['title'],
                    isbn=self.generate_isbn(item['isbn']),
                    total_pages=self.generate_pages(item['pages']),
                    amount=self.generate_amount(),
                    publishing_year=self.generate_publishing_year(item['publishing_year']),
                    publisher_id=self.generate_publisher_id(item['publisher']),
                    price=self.generate_price(),
                    annotation=item['annotation'],
                    cover_path=item['cover_path'],
                    library_location=self.generate_library_location())


    def generate_books(self, container):
        books = list()
        for item in container:
            book = self.generate_book(item)
            books.append(book)
            
        return books

    def generate(self, container=list()):
        self.container = self.generate_books(container)
