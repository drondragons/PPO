from datetime import date
from validator import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    title: str = Validator(str, [Validator.exist_validator])
    isbn: str = Validator(str, [Validator.exist_validator,
                                Validator.symbols_validator,
                                Validator.length_validator],
                          13, 13, '[^\d\-]')
    total_pages: int = Validator(int, [Validator.exist_validator,
                                       Validator.interval_validator],
                                 4)
    amount: int = Validator(int, [Validator.exist_validator,
                                  Validator.interval_validator],
                            0)
    publishing_year: int = Validator(int, [Validator.exist_validator,
                                           Validator.interval_validator],
                                     1500, date.today().year)
    publisher_id: int = Validator(int, [Validator.exist_validator,
                                        Validator.interval_validator],
                                  1)
    price: int = Validator(int, [Validator.exist_validator,
                                 Validator.interval_validator],
                           0)
    annotation: str = Validator(str, [])
    photo_path: str = Validator(str, [])
    library_location: str = Validato(str, [])


class BooksGenerator:
    class_type = Book
    file_path = '../TableData/Books.csv'
    default_photo_path = '../TableData/BooksPhoto/default_book_cover.png'


    def __init__(self):
        self.container = list()


    def generate(self):
        pass
        #scrapper = 
        #self.container = self.

        
    
    
