from generator_abstract import DataGenerator
from generator_authors import AuthorsGenerator
from dt_author_literary_work import AuthorLiteraryWork
from csv_handler_dataclass import CSVHandler_dataclass
from generator_literary_works import LiteraryWorksGenerator


class AuthorLiteraryWorksGenerator(DataGenerator):
    def __init__(self, path='../TableData/AuthorLiteraryWorks.csv', class_type=AuthorLiteraryWork):
        super().__init__(path, class_type)
        
        
    def generate_author_literary_work(self, index, initials, container, literary_works):
        result = list()
        literary_work = [record['path'] for record in container if record['author'] == initials]
        for i, item in enumerate(literary_works, 1):
            result += [AuthorLiteraryWork(index, i) for el in literary_work if el == item.ebook_path]
        return result
        
        
    def generate_author_literary_works(self, container):
        handler = CSVHandler_dataclass(AuthorsGenerator().path, AuthorsGenerator().class_type)
        authors = handler.get_csv_data()
        
        handler = CSVHandler_dataclass(LiteraryWorksGenerator().path, LiteraryWorksGenerator().class_type)
        literary_works = handler.get_csv_data()
        
        author_literary_works = list()
        for i, author in enumerate(authors, 1):
            author_literary_work = self.generate_author_literary_work(i, author.initials, container, literary_works)
            author_literary_works.extend(author_literary_work)
            
        return author_literary_works
        
        
    def generate(self, container=list()):
        self.container = self.generate_author_literary_works(container)