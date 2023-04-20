from validation import Validator
from dataclasses import dataclass


regex_authors_initials = '^[а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+$'
regex_authors_photos_path = '^\.\.\/TableData\/AuthorsPhoto\/[0-9а-яА-ЯёЁ\-\_]+\.(png|jpg|jpeg)$'


@dataclass(frozen=True)
class Author:
      initials: str = Validator(str, [Validator.exist_validator, Validator.match_validator, Validator.length_validator], 1, 50, regex_authors_initials)
      birth_date: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 5, 10, '[^\d\.]')
      death_date: str = Validator(str)
      photo_path: str = Validator(str, [Validator.exist_validator, Validator.match_validator], regex=regex_authors_photos_path)
      biography: str = Validator(str, [Validator.exist_validator])