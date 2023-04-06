from faker import Faker
from dataclasses import dataclass
from AttributeValidator import Validator


@dataclass(frozen=True, order=True)
class Country:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f"{self.name}"


class CountriesGenerator:
    class_type = Country
    file_path = "../TableData/Countries.csv"

    
    def __init__(self):
        self.container = list()


    def is_newCountry(self, country, countries):
        return not country in countries
    

    def generateCountry(self, fake):
        return Country(name=fake.country())


    def generateCountries(self, locale="ru_RU", limit=193):
        countries = list()
        fake = Faker(locale)
        while len(countries) < limit:
            country = self.generateCountry(fake)
            if self.is_newCountry(country, countries):
                countries.append(country)

        countries.sort()
        
        return countries
    

    def generate(self):
        self.container = self.generateCountries()

