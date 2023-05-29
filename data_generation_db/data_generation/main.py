from functions import Functions, AnswerError

from scrapper_authors import ScrapperAuthors
from scrapper_literature import ScrapperLiterature

from csv_handler_dict import CSVHandler_dict
from csv_handler_dataclass import CSVHandler_dataclass

from generator_users import UsersGenerator
from generator_roles import RolesGenerator
from generator_books import BooksGenerator
from generator_genres import GenresGenerator
from generator_authors import AuthorsGenerator
from generator_statuses import StatusesGenerator
from generator_countries import CountriesGenerator
from generator_languages import LanguagesGenerator
from generator_publishers import PublishersGenerator
from generator_book_records import BookRecordsGenerator
from generator_literary_works import LiteraryWorksGenerator
from generator_book_literary_works import BookLiteraryWorksGenerator
from generator_literary_work_genres import LiteraryWorkGenresGenerator
from generator_author_literary_work import AuthorLiteraryWorksGenerator


def is_literature_scrapper(generator):
    return type(generator) in [BooksGenerator, LiteraryWorksGenerator,
                               GenresGenerator, BookLiteraryWorksGenerator,
                               LiteraryWorkGenresGenerator, AuthorLiteraryWorksGenerator]


def check_dir_existence(dirs):
    for path in dirs:
        if not Functions.is_exist_file(path):
            Functions.create_dir(path)


def is_need_to_recreate(file):
    return (not Functions.is_exist_file(file)) or (Functions.choose_menu_point(file) == 1)


def run_scrappers(scrappers):
    for scrapper, file in scrappers.items():
        if is_need_to_recreate(file):
            data = scrapper().get_data()
            CSVHandler_dict(file, data[0].keys()).write_csv(data)
   
   
def format_records(records, key, func):
    for record in records:
        record[key] = func(record[key])
     
     
def run_generators(generators, scrappers):
    handler = CSVHandler_dict(scrappers[ScrapperAuthors])
    authors_records = handler.get_csv_data(is_header=True)

    handler = CSVHandler_dict(scrappers[ScrapperLiterature])
    literature_records = handler.get_csv_data(is_header=True)
    format_records(literature_records, 'genre', Functions.convert_str_to_list)
    
    for generator in generators:
        generator = generator()
        if is_need_to_recreate(generator.path):
            records = list()
            if isinstance(generator, AuthorsGenerator):
                records = authors_records
            elif is_literature_scrapper(generator):
                records = literature_records
            
            generator.generate(records)
            
            handler = CSVHandler_dataclass(generator.path, generator.class_type)
            handler.write_csv(generator.container)
            
            print(f'\nФайл {generator.path!r} создан и заполнен!\n')
        
    print('\nВсе файлы созданы и заполнены!\n')
        
        
            
def main():
    dirs = ['../TableData',
            '../TableData/AuthorsPhoto',
            '../TableData/BooksPhoto',
            '../TableData/BooksEpub',
            '../TableData/WebsiteRecords']
    
    scrappers = {ScrapperAuthors: '../TableData/WebsiteRecords/authors_records.csv',
                 ScrapperLiterature: '../TableData/WebsiteRecords/literarture_records.csv'}
    
    generators = [RolesGenerator, StatusesGenerator,
                  CountriesGenerator, LanguagesGenerator,
                  UsersGenerator, PublishersGenerator,
                  AuthorsGenerator, GenresGenerator,
                  BooksGenerator, LiteraryWorksGenerator,
                  LiteraryWorkGenresGenerator, AuthorLiteraryWorksGenerator,
                  BookLiteraryWorksGenerator, BookRecordsGenerator]
    
    try:
        check_dir_existence(dirs)
        
        run_scrappers(scrappers)
        run_generators(generators, scrappers)
        
    except OSError as error:
        print(f'\nНе удалось создать папку \'{error}\'!\n\
Проверьте название папки или права доступа!\n')
        
    except AnswerError as error:
        print(error)
        
    except ValueError as error:
        print(error)
    
    except KeyboardInterrupt:
        print('\nПрограмма остановлена сочетанием клавиш <CTRL + C>!\n')
        
    except Exception as error:
        print(error)
    
    finally:
        input()
    
        
if __name__ == '__main__':
    main()
