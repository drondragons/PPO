from abc import ABC, abstractmethod


class ICSVHandler(ABC):
    def __init__(self, path, encoding='utf-8', delimiter='|', newline=''):
        self.path = path
        self.newline = newline
        self.encoding = encoding
        self.delimiter = delimiter


    @abstractmethod
    def show_csv(self):
        pass


    @abstractmethod
    def get_csv_data(self, open_type='r'):
        pass


    @abstractmethod
    def write_csv(self, data, open_type='w'):
        pass


    @abstractmethod
    def add_data_in_csv(self, input_data):
        pass