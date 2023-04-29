from datetime import date
from validation import Validator
from dataclasses import dataclass


regex_books_photos_path = '^\.\.\/TableData\/BooksPhoto\/[0-9а-яА-ЯёЁa-zA-Z\-\_]+\.(png|jpg|jpeg)$'


@dataclass(frozen=True, order=True)
class Book:
      title: str = Validator(str, [Validator.exist_validator])
      isbn: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 15, 17, '[^\d\-]')
      total_pages: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 4)
      amount: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 0)
      publishing_year: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1500, date.today().year)
      publisher_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
      price: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 0)
      annotation: str = Validator(str, [Validator.exist_validator])
      cover_path: str = Validator(str, [Validator.exist_validator, Validator.match_validator], regex=regex_books_photos_path)
      library_location: str = Validator(str, [Validator.exist_validator])