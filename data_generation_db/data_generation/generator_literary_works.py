from datetime import date

from dt_literary_work import LiteraryWork
from generator_abstract import DataGenerator
from generator_authors import AuthorsGenerator, Author

from scrapper_authors import ScrapperAuthors

from csv_handler_dataclass import CSVHandler_dataclass


class LiteraryWorksGenerator(DataGenerator):
    def __init__(self, path='../TableData/LiteraryWorks.csv', class_type=LiteraryWork):
        super().__init__(path, class_type)


    def generate_writing_year(self, item):
        handler = CSVHandler_dataclass(AuthorsGenerator().path, AuthorsGenerator().class_type)
        authors = handler.get_csv_data()

        writing_year = item['writing_year']
        if not writing_year:
            year = [author.death_date for author in authors if author.initials == item['author']]
            writing_year = int(year[0].split('.')[-1]) - 1 if year else date.today().year - 1
            
        return int(writing_year)
        
        
    def generate_biography(self, initials):
        return f'{initials} - писатель. Биография по умолчанию.'    
        
        
    def generate_author(self, initials):
        return Author(initials=initials,
                      birth_date='',
                      death_date='',
                      photo_path=ScrapperAuthors.default_author_photo,
                      biography=self.generate_biography(initials))
        
        
    def add_author(self, initials, authors):
        names = [author.initials for author in authors]
        if initials not in names:
            authors.append(self.generate_author(initials))
        

    def generate_literary_work(self, item, authors):
        self.add_author(item['author'], authors)
        
        return LiteraryWork(title=item['title'],
                            writing_year=self.generate_writing_year(item),
                            description=item['description'],
                            ebook_path=item['path'])


    def generate_literary_works(self, container):
        handler = CSVHandler_dataclass(AuthorsGenerator().path, AuthorsGenerator().class_type)
        authors = handler.get_csv_data()
        
        literary_works = list()
        for item in container:
            literary_work = self.generate_literary_work(item, authors)
            literary_works.append(literary_work)
            
        handler.write_csv(authors)

        return literary_works


    def generate(self, container=list()):
        self.container = self.generate_literary_works(container)
