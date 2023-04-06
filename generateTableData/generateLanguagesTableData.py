from faker import Faker
from dataclasses import dataclass
from AttributeValidator import Validator


@dataclass(frozen=True, order=True)
class Language:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f"{self.name}"


class LanguagesGenerator:
    class_type = Language
    file_path = "../TableData/Languages.csv"

    
    def __init__(self):
        self.container = list()


    def is_newLanguage(self, language, languages):
        return not language in languages
    

    def generateLanguage(self, fake):
        return Language(name=fake.language_name())


    def generateLanguages(self, locale="ru_RU", limit=127):
        languages = list()
        fake = Faker(locale)
        while len(languages) < limit:
            language = self.generateLanguage(fake)
            if self.is_newLanguage(language, languages):
                languages.append(language)

        languages.sort()
        
        return languages
    

    def generate(self):
        self.container = self.generateLanguages()
