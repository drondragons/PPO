from dt_publisher import Publisher
from generator_abstract import DataGenerator
from generator_countries import CountriesGenerator
from csv_handler_dataclass import CSVHandler_dataclass


class PublishersGenerator(DataGenerator):
    def __init__(self, path='../TableData/Publishers.csv', class_type=Publisher):
        super().__init__(path, class_type)


    def generate_country_id(self):
        handler = CSVHandler_dataclass(CountriesGenerator().path, CountriesGenerator().class_type)
        countries = handler.get_csv_data()

        return [i for i, country in enumerate(countries, 1) if country.name == 'Россия'][0] 


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
            

    def generate(self, container=list()):
        self.container = self.generate_publishers()