from validation import Validator
from dataclasses import dataclass
from scrapper_authors import ScrapperAuthors


@dataclass(frozen=True)
class Author:
    initials: str = Validator(str, [Validator.exist_validator,
                                    Validator.match_validator,
                                    Validator.length_validator],
                              1, 50, '^[а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+$')
    birth_date: str = Validator(str, [Validator.exist_validator,
                                      Validator.symbols_validator,
                                      Validator.length_validator],
                                5, 10, '[^\d\.]')
    death_date: str = Validator(str, [])
    photo_path: str = Validator(str, [Validator.exist_validator,
                                      Validator.match_validator],
                                regex='^\.\.\/TableData\/AuthorsPhoto\/[0-9а-яА-ЯёЁ\-\_]+\.(png|jpg|jpeg)$')
    biography: str = Validator(str, [Validator.exist_validator])


class AuthorsGenerator:
    class_type = Author
    file_path = '../TableData/Authors.csv'


    def __init__(self):
        self.container = list()


    def generate(self):
        self.container = ScrapperAuthors().get_authors()
