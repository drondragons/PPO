from abc import ABC, abstractmethod
from dataclass_csv import DataclassWriter, DataclassReader


class ICSVHandler(ABC):
    def __init__(self, path, encoding="utf-8", delimiter="|", newline=""):
        self.path = path
        self.newline = newline
        self.encoding = encoding
        self.delimiter = delimiter


    @abstractmethod
    def show_csv(self):
        pass


    @abstractmethod
    def get_csv_data(self, open_type="r"):
        pass


    @abstractmethod
    def write_csv(self, data, open_type="w"):
        pass


    @abstractmethod
    def add_data_in_csv(self, input_data):
        pass
    

class CSVHandler_dataclass(ICSVHandler):
    def __init__(self, path, class_type, encoding="utf-8", delimiter="|",
                 newline=""):
        self.class_type = class_type
        super().__init__(path, encoding, delimiter, newline)
        
        
    def write_csv(self, data, open_type="w", is_header=False):
        try:
            with open(self.path, open_type, encoding=self.encoding,
                      newline=self.newline) as file:
                csv_writer = DataclassWriter(file, data, self.class_type,
                                             delimiter=self.delimiter)
                csv_writer.write(skip_header=is_header)

        except OSError:
            raise OSError(f"\nНе удалось открыть файл {self.path!r}!\n\
Проверьте название файла или права доступа!\n")

        except ValueError:
            raise ValueError("\nНекорректный тип входных данных для записи\
 в csv файл!\n")        

        except Exception as error:
            raise Exception(f"\nОшибка: {error!r}\n")
            

    def get_csv_data(self, open_type="r"):
        csv_data = list()
        try:
            with open(self.path, open_type, encoding=self.encoding,
                      newline=self.newline) as file:
                csv_reader = DataclassReader(file, self.class_type,
                                             delimiter=self.delimiter,
                                             validate_header=False)
                for row in csv_reader:
                    csv_data.append(row)

        except OSError:
            raise OSError(f"\nНе удалось открыть файл {self.path!r}!\n\
Проверьте название файла или права доступа!\n")
        
        except Exception as error:
            raise Exception(f"\nОшибка: {error!r}\n")
        
        return csv_data


    def show_csv(self):
        try:
            with open(self.path, "r", encoding=self.encoding,
                      newline=self.newline) as file:
                csv_reader = DataclassReader(file, self.class_type,
                                             delimiter=self.delimiter)
                for row in csv_reader:
                    print(row)

            print()
            
        except OSError:
            raise OSError(f"\nНе удалось открыть файл {self.path!r}!\n\
Проверьте название файла или права доступа!\n")
        
        except Exception as error:
            raise Exception(f"\nОшибка: {error!r}\n")


    def add_row(self, input_data):
        csv_data = self.get_csv_data()
        if not input_data in csv_data:
            self.write_csv([input_data], "a", True)


    def add_rows(self, input_data):
        csv_data = self.get_csv_data()
        for element in input_data:
            self.add_row(element)
        

    def add_data_in_csv(self, input_data):
        is_obj_list = input_data and isinstance(input_data, list) and \
           isinstance(input_data[0], self.class_type)
        is_obj = input_data and isinstance(input_data, self.class_type)
        if is_obj:
            self.add_row(input_data)
            
        elif is_obj_list:
            self.add_rows(input_data)
            
        else:
            raise ValueError("\nНекорректный тип входных данных для добавления\
 в csv файл!\n")
