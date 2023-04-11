from validation import Validator
from dataclasses import dataclass
from csv_handler import CSVHandler_dataclass
from generate_countries import CountriesGenerator


@dataclass(frozen=True, order=True)
class Publisher:
    name: str = Validator(str, [Validator.exist_validator])
    country_id: int = Validator(int, [Validator.exist_validator])


class PublishersGenerator:
    class_type = Publisher
    file_path = '../TableData/Publishers.csv'

    
    def __init__(self):
        self.container = list()


    def generate_country_id(self):
        handler = CSVHandler_dataclass(CountriesGenerator.file_path,
                                       CountriesGenerator.class_type)
        countries = handler.get_csv_data()

        country_id = 1
        country_name = 'Россия'
        for i, country in enumerate(countries, 1):
            if country.name == country_name:
                country_id = i
                break

        return country_id


    def generate_publishers(self):
        russia = self.generate_country_id()
        publishers = [Publisher(name='АСТ', country_id=russia),
                      Publisher(name='Астрель', country_id=russia),
                      Publisher(name='Эксмо', country_id=russia),
                      Publisher(name='Правда', country_id=russia),
                      Publisher(name='МИФ', country_id=russia),
                      Publisher(name='Качели', country_id=russia),
                      Publisher(name='Менеджер', country_id=russia),
                      Publisher(name='Омега', country_id=russia),
                      Publisher(name='Гамма', country_id=russia),
                      Publisher(name='Самовар-книги', country_id=russia),
                      Publisher(name='КомпасГид', country_id=russia),
                      Publisher(name='Клевер-Медиа-Групп', country_id=russia),
                      Publisher(name='Азбука-Аттикус', country_id=russia),
                      Publisher(name='Феникс', country_id=russia),
                      Publisher(name='Диалектика', country_id=russia),
                      Publisher(name='Проспект', country_id=russia),
                      Publisher(name='Просвещение', country_id=russia),
                      Publisher(name='Искателькнига', country_id=russia),
                      Publisher(name='Детская литература', country_id=russia),
                      Publisher(name='Стрекоза', country_id=russia),
                      Publisher(name='Голден-Би', country_id=russia)]
        publishers.sort()

        return publishers
            

    def generate(self):
        self.container = self.generate_publishers()
