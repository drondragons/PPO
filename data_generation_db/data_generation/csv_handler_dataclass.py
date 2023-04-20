from csv_handler_abstract import ICSVHandler
from dataclass_csv import DataclassWriter, DataclassReader
    

class CSVHandler_dataclass(ICSVHandler):
    def __init__(self, path, class_type, encoding='utf-8', delimiter='|', newline=''):
        self.class_type = class_type
        super().__init__(path, encoding, delimiter, newline)
        
        
    def write_csv(self, data, open_type='w', is_header=False):
        with open(self.path, open_type, encoding=self.encoding, newline=self.newline) as f:
            writer = DataclassWriter(f, data, self.class_type, delimiter=self.delimiter)
            writer.write(skip_header=is_header)
            

    def get_csv_data(self, open_type='r'):
        data = list()
        with open(self.path, open_type, encoding=self.encoding, newline=self.newline) as f:
            reader = DataclassReader(f, self.class_type, delimiter=self.delimiter, validate_header=False)
            for row in reader:
                data.append(row)
        
        return data


    def show_csv(self):
        with open(self.path, 'r', encoding=self.encoding, newline=self.newline) as f:
            reader = DataclassReader(f, self.class_type, delimiter=self.delimiter)
            for row in reader:
                print(row)
        print()
        
        
    def add_data_in_csv(self, input_data):
        self.write_csv([input_data], 'a', True)
