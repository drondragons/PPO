from functions import Functions
from csv_handler import CSVHandler_dataclass

from generate_roles import RolesGenerator
from generate_users import UsersGenerator
from generate_authors import AuthorsGenerator
from generate_statuses import StatusesGenerator
from generate_countries import CountriesGenerator
from generate_languages import LanguagesGenerator
from generate_publishers import PublishersGenerator

from requests.exceptions import ConnectionError, MissingSchema, InvalidURL


class Creator:
    def create_table(self, table, message):
        table.generate()
        csv_handler_dataclass = CSVHandler_dataclass(table.file_path,
                                                     table.class_type)
        csv_handler_dataclass.write_csv(table.container)
        #csv_handler_dataclass.show_csv()
        print(message)
        
    
    def create_tables(self, class_types):
        for class_type in class_types:
            table = class_type()
            if not Functions.is_exist_file(table.file_path):
                self.create_table(table, f'\nФайл {table.file_path!r} создан и\
 заполнен!\n')
            else:
                answer = Functions.choose_menu_point(table.file_path)
                if answer == 1:
                    self.create_table(table, f'\nФайл {table.file_path!r}\
 пересоздан и заполнен!\n')

        print('\nВсе файлы созданы и заполнены!\n')


def main():
    table_dir = '../TableData/'
    try:
        if not Functions.is_exist_file(table_dir):
            Functions.create_dir(table_dir)

        tables = [RolesGenerator, UsersGenerator, StatusesGenerator,
                  LanguagesGenerator, CountriesGenerator, PublishersGenerator,
                  AuthorsGenerator]
    
        creator = Creator()
        creator.create_tables(tables)

    except OSError as error:
        print(error)
        
    except ValueError as error:
        print(error)

    except TypeError as error:
        print(error)

    except ConnectionError as error:
        print(error)

    except MissingSchema as error:
        print(error)

    except InvalidURL as error:
        print(error)
    
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
