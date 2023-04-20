from faker import Faker
from dt_language import Language
from generator_abstract import DataGenerator


class LanguagesGenerator(DataGenerator):
    def __init__(self, path='../TableData/Languages.csv', class_type=Language):
        super().__init__(path, class_type)
        
    
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
    

    def generate(self, container=list()):
        self.container = self.generate_languages()
