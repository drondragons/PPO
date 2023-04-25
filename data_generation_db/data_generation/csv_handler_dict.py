from csv import DictWriter, DictReader
from csv_handler_abstract import ICSVHandler
    

class CSVHandler_dict(ICSVHandler):
    def __init__(self, path, keys=None, encoding='utf-8', delimiter='|', newline=''):
        self.keys = keys
        super().__init__(path, encoding, delimiter, newline)
        
        
    def write_csv(self, data, open_type='w', is_header=True):
        with open(self.path, open_type, encoding=self.encoding, newline=self.newline) as f:
            writer = DictWriter(f, self.keys, delimiter=self.delimiter)
            if is_header:
                writer.writeheader()
            writer.writerows(data)
            

    def get_csv_data(self, open_type='r', is_header=False):
        data = list()
        with open(self.path, open_type, encoding=self.encoding, newline=self.newline) as f:
            reader = DictReader(f, delimiter=self.delimiter)
            if not is_header:
                next(reader)
            for row in reader:
                data.append(row)
        
        return data


    def show_csv(self):
        with open(self.path, 'r', encoding=self.encoding, newline=self.newline) as f:
            reader = DictReader(f, delimiter=self.delimiter)
            next(reader)
            for row in reader:
                print(row)
        print()
        
        
    def add_data_in_csv(self, input_data):
        self.write_csv(input_data, 'a', False)
