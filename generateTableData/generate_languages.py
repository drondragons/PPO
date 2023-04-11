from faker import Faker
from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Language:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f'{self.name}'


class LanguagesGenerator:
    class_type = Language
    file_path = '../TableData/Languages.csv'

    
    def __init__(self):
        self.container = list()


    def is_new_language(self, language, languages):
        return not language in languages
    

    def generate_language(self, fake):
        return Language(name=fake.language_name())


    def generate_languages(self, locale='ru_RU', limit=127):
        languages = list()
        fake = Faker(locale)
        while len(languages) < limit:
            language = self.generate_language(fake)
            if self.is_new_language(language, languages):
                languages.append(language)

        languages.sort()
        
        return languages
    

    def generate(self):
        self.container = self.generate_languages()
