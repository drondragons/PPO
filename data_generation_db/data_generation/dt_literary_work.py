from datetime import date
from validation import Validator
from dataclasses import dataclass


regex_books_epub_path = '^\.\.\/TableData\/BooksEpub\/[0-9а-яА-ЯёЁa-zA-Z\-\_]+\.epub$'


@dataclass(frozen=True)
class LiteraryWork:
    title: str = Validator(str, [Validator.exist_validator])
    writing_year: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1, date.today().year)
    description: str = Validator(str, [Validator.exist_validator])
    ebook_path: str = Validator(str, [Validator.exist_validator, Validator.match_validator], regex=regex_books_epub_path)