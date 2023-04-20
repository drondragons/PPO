from datetime import date
from dt_literary_work import LiteraryWork
from generator_abstract import DataGenerator
from generator_authors import AuthorsGenerator
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
            writing_year = int(year[0].split('.')[-1]) - 1 if year[0] else date.today().year - 1

        return writing_year
        

    def generate_literary_work(self, item):
        return LiteraryWork(title=item['title'],
                            writing_year=self.generate_writing_year(item),
                            description=item['description'],
                            ebook_path=item['path'])


    def generate_literary_works(self, container):
        literary_works = list()
        for item in container:
            literary_work = self.generate_literary_work(item)
            literary_works.append(literary_work)

        return literary_works


    def generate(self, container=list()):
        self.container = self.generate_literary_works(container)
