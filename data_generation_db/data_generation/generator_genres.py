from dt_genre import Genre
from functions import Functions
from generator_abstract import DataGenerator


class GenresGenerator(DataGenerator):
    def __init__(self, path='../TableData/Genres.csv', class_type=Genre):
        super().__init__(path, class_type)
        
        
    def generate_description(self, name):
        return f'Описание жанра {name.lower()} по умолчанию.'


    def generate_genre(self, record, genres):
        result = list()
        for item in record:
            genre = Genre(title=item,
                          description=self.generate_description(item))
            if genre not in genres:
                result.append(genre)
                
        return result
        

    def generate_genres(self, container):
        genres = list()
        for record in container:
            record['genre'] = Functions.convert_str_to_list(record['genre'])
            genre = self.generate_genre(record['genre'], genres)
            genres.extend(genre)
            
        return genres


    def generate(self, container=list()):
        self.container = self.generate_genres(container)
