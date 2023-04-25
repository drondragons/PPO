from dt_author import Author
from generator_abstract import DataGenerator


class AuthorsGenerator(DataGenerator):
    def __init__(self, path='../TableData/Authors.csv', class_type=Author):
        super().__init__(path, class_type)


    def generate_death_date(self, date):
        return date if date else ''


    def generate_author(self, item):
        return Author(initials=item['initials'],
                      birth_date=item['birth_date'],
                      death_date=self.generate_death_date(item['death_date']),
                      photo_path=item['photo_path'],
                      biography=item['biography'])
        

    def generate_authors(self, container):
        authors = list()
        for item in container:
            author = self.generate_author(item)
            authors.append(author)
            
        return authors
    

    def generate(self, container=list()):
        self.container = self.generate_authors(container)