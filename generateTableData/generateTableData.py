from HandlerCSV import CSVHandler_dataclass
from generalFunctions import GeneralFunctions

from generateRolesTableData import RolesGenerator
from generateUsersTableData import UsersGenerator
from generateAuthorsTableData import AuthorsGenerator
from generateStatusesTableData import StatusesGenerator
from generateCountriesTableData import CountriesGenerator
from generateLanguagesTableData import LanguagesGenerator
from generatePublishersTableData import PublishersGenerator

from requests.exceptions import ConnectionError, MissingSchema, InvalidURL


class Creator:
    def createTable(self, table, message):
        table.generate()
        csv_handler_dataclass = CSVHandler_dataclass(table.file_path,
                                                     table.class_type)
        csv_handler_dataclass.writeCSV(table.container)
        #csv_handler_dataclass.showCSV()
        print(message)
        
    
    def createTables(self, class_types):
        for class_type in class_types:
            table = class_type()
            if not GeneralFunctions.is_existFile(table.file_path):
                self.createTable(table, f"\nФайл {table.file_path!r} создан и\
 заполнен!\n")
            else:
                answer = GeneralFunctions.chooseMenuPoint(table.file_path)
                if answer == 1:
                    self.createTable(table, f"\nФайл {table.file_path!r}\
 пересоздан и заполнен!\n")

        print("\nВсе файлы созданы и заполнены!\n")


def main():
    table_dir = "../TableData/"
    try:
        if not GeneralFunctions.is_existFile(table_dir):
            GeneralFunctions.createDir(table_dir)

        tables = [RolesGenerator, UsersGenerator, StatusesGenerator,
                  LanguagesGenerator, CountriesGenerator, PublishersGenerator,
                  AuthorsGenerator]
    
        creator = Creator()
        creator.createTables(tables)

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
