import re
import os


class AnswerError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Functions:
    @staticmethod
    def is_exist_file(file_path):
        return os.path.exists(file_path)


    @staticmethod
    def create_dir(dir_path):
        try:
            os.makedirs(dir_path)
            
        except OSError:
            raise OSError(dir_path)


    @staticmethod
    def replace(what, on_what, src):
        return re.sub(what, on_what, src)


    @staticmethod
    def replace_html_symbols(src):
        symbols = {' ': r'\s+',
                   '-': r'[-‑—–]+',
                   '...': r'[…]+',
                   '': r'[¬]+',
                   '«': r'[“]+',
                   '»': r'[”]+',
                   'е': r'[ё]+',
                   'Е': r'[Ё]+'}
        for key, value in symbols.items():
            src = Functions.replace(value, key, src)

        out = str()
        is_find = False
        for c in src:
            if c == '"':
                c = '»' if is_find else '«'
                is_find = not is_find
            out += c
                
        return out
    

    @staticmethod
    def swap_name_surname(src):
        return '{1} {0}'.format(*src.split(' '))


    @staticmethod
    def get_unused_path(src):
        index = 1
        path = src.format(index=index)
        while Functions.is_exist_file(path):
            index += 1
            path = src.format(index=index)

        return path


    @staticmethod
    def save_bytes_file(path, content):
        with open(path, 'wb') as f:
            f.write(content)
       
    
    @staticmethod
    def get_answer(message='Введите число: '):
        return int(input(message))
        

    @staticmethod
    def choose_menu_point(file):
        menu = f'Выберите вариант ответа:\
\n\t1. Пересоздать файл {file!r};\
\n\t2. Оставить файл без изменений.\
\n\nНомер варианта ответа: '

        answer = Functions.get_answer(menu)
        if not 1 <= answer <= 2:
            raise AnswerError('\nВыбран неизвестный пункт!\n')
        print('='*60)
        print()
        
        return answer
    
    
    @staticmethod
    def convert_str_to_list(src):
        return re.sub(r'[\[\]\']+', '', src).split(', ')