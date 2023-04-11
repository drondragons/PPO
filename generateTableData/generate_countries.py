from faker import Faker
from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Country:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f'{self.name}'


class CountriesGenerator:
    class_type = Country
    file_path = '../TableData/Countries.csv'

    
    def __init__(self):
        self.container = list()


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
    

    def generate(self):
        self.container = self.generate_countries()
