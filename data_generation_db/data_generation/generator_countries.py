from faker import Faker
from dt_country import Country
from generator_abstract import DataGenerator


class CountriesGenerator(DataGenerator):
    def __init__(self, path='../TableData/Countries.csv', class_type=Country):
        super().__init__(path, class_type)


    def is_new_country(self, country, countries):
        return not country in countries
    

    def generate_country(self, fake):
        return Country(name=fake.country())


    def generate_countries(self, locale='ru_RU', limit=193):
        countries = list()
        fake = Faker(locale)
        while len(countries) < limit:
            country = self.generate_country(fake)
            if self.is_new_country(country, countries):
                countries.append(country)

        countries.sort()
        
        return countries
    

    def generate(self, container=list()):
        self.container = self.generate_countries()