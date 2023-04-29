import random
import datetime

from dt_book_record import BookRecord

from generator_roles import RolesGenerator
from generator_users import UsersGenerator
from generator_books import BooksGenerator
from generator_abstract import DataGenerator
from generator_statuses import StatusesGenerator

from csv_handler_dataclass import CSVHandler_dataclass


class BookRecordsGenerator(DataGenerator):
    def __init__(self, path='../TableData/BookRecords.csv', class_type=BookRecord):
        super().__init__(path, class_type)
        
        
    def find_entity_by_attribute(self, entities, attribute):
        d = dict()
        for i, entity in enumerate(entities, 1):
            d.setdefault(getattr(entity, attribute), i)
        return d
        
    
    def find_user_by_role(self, roles, users, value):
        return [[i, user] for i, user in enumerate(users, 1) if user.role_id == roles[value]]
    
    
    def find_users_by_role(self, users, roles):
        users_by_role = dict.fromkeys(roles.keys(), list())
        for key in users_by_role:
            users_by_role[key] = self.find_user_by_role(roles, users, key)
        return users_by_role
        
        
    def generate_user_id(self, users):
        return random.choice(users)[0]
        
       
    def generate_book(self, books):
        return random.choice(books)   
        
        
    def generate_book_record(self, users, book, status, date):
        book_id = book[0]
        book_amount = book[1].amount
        return BookRecord(user_id=self.generate_user_id(users),
                          book_id=book_id,
                          book_status_id=status,
                          book_amount=book_amount,
                          date=date.strftime('%H:%M:%S %d.%m.%Y'))
        
        
    def generate_date(self, date):
        next_date = date + datetime.timedelta(hours=random.randint(1, 4), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
        if not 8 <= next_date.hour <= 19:
            next_date = date + datetime.timedelta(days=1)
            next_date = datetime.datetime(year=next_date.year, month=next_date.month, day=next_date.day,
                                          hour=random.randint(8, 19), minute=random.randint(0,59), second=random.randint(0, 59))
        return next_date
    
        
    def generate_book_records_on_add(self, users, statuses, books, date):
        add_status = statuses.get('добавлено')
        library_workers = users.get('библиотекарь') + users.get('администратор')
        
        result = list()
        books_in_library = books.copy()
        iterations = random.randint(len(books) // 2, len(books))
        for _ in range(iterations):
            book = self.generate_book(books_in_library)
            books_in_library.remove(book)
            result.append(self.generate_book_record(library_workers, book, add_status, date))
            date = self.generate_date(date)
            
        return result             


    def find_book_by_book_id(self, books, book_id):
        return [book for book in books if book_id == book[0]][0]
    
    
    def generate_book_record_on_hand(self, user_id, book, status, book_record, book_amount):
        result = list()
        date = self.generate_date(datetime.datetime.strptime(book_record.date, '%H:%M:%S %d.%m.%Y'))
        if 0 <= book[2] - book_amount <= book[1].amount:
            if status not in ['забронировано', 'отменено бронирование']:
                book[2] -= book_amount            
            result = [BookRecord(user_id=user_id,
                                 book_id=book[0],
                                 book_status_id=status,
                                 book_amount=abs(book_amount),
                                 date=date.strftime('%H:%M:%S %d.%m.%Y'))]
        
        return result
            
        
    def generate_book_record_on_hands(self, readers, statuses, books_in_library, book_record):
        book = self.find_book_by_book_id(books_in_library, book_record.book_id)
        
        status = 0
        user_id = book_record.user_id
        book_amount = random.randint(1, 3)
        if book_record.book_status_id in [statuses.get('добавлено'),  statuses.get('отменено бронирование'), statuses.get('возвращено')]:
            user_id = self.generate_user_id(readers)
            status = random.choice([statuses.get('забронировано'), statuses.get('выдано')])   
        elif book_record.book_status_id == statuses.get('забронировано'):
            status = random.choice([statuses.get('отменено бронирование'), statuses.get('выдано')])
            book_amount = book_record.book_amount
        elif book_record.book_status_id == statuses.get('выдано'):
            status = statuses.get('возвращено')
            book_amount = -book_record.book_amount
        
        return self.generate_book_record_on_hand(user_id, book, status, book_record, book_amount)
        
                
    def generate_book_records_on_hands(self, users, statuses, books_in_library, book_records):
        readers = users.get('читатель')
        iterations = random.randint(len(books_in_library), len(books_in_library) * 2)
        for _ in range(iterations):
            book_records_for_choice = book_records.copy()
            book_record = random.choice(book_records_for_choice)
            book_records_for_choice.remove(book_record)
            book_records.extend(self.generate_book_record_on_hands(readers, statuses, books_in_library, book_record))
        
        return book_records
        
        
    def find_added_books(self, books, records):
        return [book for record in records for book in books if record.book_id == book[0]]   
        
    
    @staticmethod    
    def sort_date(book_record):
        return datetime.datetime.strptime(book_record.date, '%H:%M:%S %d.%m.%Y')     
        
        
    def generate_book_records(self, users, statuses, books):
        date = datetime.datetime(2022, 6, 1, 8, random.randint(0, 59), random.randint(0, 59))
        result = self.generate_book_records_on_add(users, statuses, books, date)
        
        records = self.find_added_books(books, result)
        result = self.generate_book_records_on_hands(users, statuses, records, result)
        
        result.sort(key=BookRecordsGenerator.sort_date)

        return result
        
        
    def get_books_index(self, books): 
        return [[index, book, book.amount] for index, book in enumerate(books, 1)]   
        
        
    def generate_records(self):
        handler = CSVHandler_dataclass(BooksGenerator().path, BooksGenerator().class_type)
        books = handler.get_csv_data()
        books = self.get_books_index(books)
        
        handler = CSVHandler_dataclass(StatusesGenerator().path, StatusesGenerator().class_type)
        statuses = handler.get_csv_data()
        statuses = self.find_entity_by_attribute(statuses, 'name')
        
        handler = CSVHandler_dataclass(UsersGenerator().path, UsersGenerator().class_type)
        users = handler.get_csv_data()
        
        handler = CSVHandler_dataclass(RolesGenerator().path, RolesGenerator().class_type)
        roles = handler.get_csv_data()
        roles = self.find_entity_by_attribute(roles, 'name')
        
        users_by_role = self.find_users_by_role(users, roles)
        result = self.generate_book_records(users_by_role, statuses, books)
        
        return result
        
        
    def generate(self, container=list()):
        self.container = self.generate_records()