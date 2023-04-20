from functions import Functions
from scrapper_authors import ScrapperAuthors
from scrapper_literature import ScrapperLiterature
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


def is_need_scrapper(generator):
    return type(generator) in [BooksGenerator,
                               LiteraryWorksGenerator,
                               GenresGenerator,
                               AuthorsGenerator]


def is_literature_scrapper(generator):
    return type(generator) in [BooksGenerator,
                               LiteraryWorksGenerator,
                               GenresGenerator,
                               BookLiteraryWorksGenerator,
                               LiteraryWorkGenresGenerator,
                               AuthorLiteraryWorksGenerator]


def need_to_scrap(generator, is_scrap, authors_records, literature_records):
    if (not is_scrap) and (is_need_scrapper(generator)):
        authors_records.extend(ScrapperAuthors().get_authors())
        literature_records.extend(ScrapperLiterature().get_literature())
        is_scrap = True

    return is_scrap
    

def create_table(generator, is_scrap, authors_records, literature_records):
    container = list()
    
    is_scrap = need_to_scrap(generator, is_scrap, authors_records, literature_records)

    if isinstance(generator, AuthorsGenerator):
        container = authors_records
    elif is_literature_scrapper(generator):
        container = literature_records

    generator.generate(container)
    
    csv_handler_dataclass = CSVHandler_dataclass(generator.path, generator.class_type)
    csv_handler_dataclass.write_csv(generator.container)

    return is_scrap
      

def create_tables(generators):
    is_scrap = False
    authors_records = literature_records = list()
    for item in generators:
        generator = item()
        if not Functions.is_exist_file(generator.path):
            is_scrap = create_table(generator, is_scrap, authors_records, literature_records)
            print(f'\nФайл {generator.path!r} создан и заполнен!\n')
        
        else:
            answer = Functions.choose_menu_point(generator.path)
            if answer == 1:
                is_scrap = create_table(generator, is_scrap, authors_records, literature_records)
                print(f'\nФайл {generator.path!r} пересоздан и заполнен!\n')

    print('\nВсе файлы созданы и заполнены!\n')


def check_dir_existence(dirs):
    for path in dirs:
        if not Functions.is_exist_file(path):
            Functions.create_dir(path)


def main():
    dirs = ['../TableData',
            '../TableData/AuthorsPhoto',
            '../TableData/BooksPhoto',
            '../TableData/BooksEpub']
    try:
        check_dir_existence(dirs)
        
        generators = [RolesGenerator, StatusesGenerator,
                      CountriesGenerator, LanguagesGenerator,
                      UsersGenerator, PublishersGenerator,
                      AuthorsGenerator, GenresGenerator,
                      BooksGenerator, LiteraryWorksGenerator,
                      LiteraryWorkGenresGenerator,
                      AuthorLiteraryWorksGenerator,
                      BookLiteraryWorksGenerator,
                      BookRecordsGenerator]
        create_tables(generators)
        
    except OSError as error:
        print(error)
        
    except ValueError as error:
        print(error)

    except TypeError as error:
        print(error)
    
    except Exception as error:
        print(error)
        
    finally:
        input()

        
if __name__ == '__main__':
    main()
