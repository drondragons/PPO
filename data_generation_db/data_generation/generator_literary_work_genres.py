from functions import Functions

from generator_genres import GenresGenerator
from generator_abstract import DataGenerator
from dt_literary_work_genre import LiteraryWorkGenre
from generator_literary_works import LiteraryWorksGenerator

from csv_handler_dataclass import CSVHandler_dataclass



class LiteraryWorkGenresGenerator(DataGenerator):
    def __init__(self, path='../TableData/LiteraryWorkGenres.csv', class_type=LiteraryWorkGenre):
        super().__init__(path, class_type)


    def generate_literary_work_genre(self, index, title, container, genres):
        result = list()
        genre = [r for record in container if record['title'] == title for r in Functions.convert_str_to_list(record['genre'])]
        for i, item in enumerate(genres, 1):
            result += [LiteraryWorkGenre(index, i) for el in genre if el == item.title]
            
        return result
    

    def generate_literary_work_genres(self, container):
        handler = CSVHandler_dataclass(GenresGenerator().path, GenresGenerator().class_type)
        genres = handler.get_csv_data()
        
        handler = CSVHandler_dataclass(LiteraryWorksGenerator().path, LiteraryWorksGenerator().class_type)
        literary_works = handler.get_csv_data()
        
        literary_work_genres = list()
        for i, literary_work in enumerate(literary_works, 1):
            literary_work_genre = self.generate_literary_work_genre(i, literary_work.title, container, genres)
            literary_work_genres.extend(literary_work_genre)
            
        return literary_work_genres


    def generate(self, container=list()):
        self.container = self.generate_literary_work_genres(container)    