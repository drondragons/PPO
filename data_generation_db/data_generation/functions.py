import re
import os


class Functions:
    @staticmethod
    def is_exist_file(file_path):
        return os.path.exists(file_path)


    @staticmethod
    def create_dir(dir_path):
        try:
            os.makedirs(dir_path)

        except:
            raise OSError(f'\nНе удалось создать папку {dir_path!r}!\n\
Проверьте название папки или права доступа!\n')


    @staticmethod
    def replace(what, on_what, src):
        return re.sub(what, on_what, src)


    @staticmethod
    def replace_html_spaces(src):
        return Functions.replace(r'\s+', ' ', src)


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
    def choose_menu_point(file_path):
        answer = int(0)
        menu = f'Выберите вариант ответа:\
\n\t1. Пересоздать файл {file_path!r};\
\n\t2. Оставить файл без изменений.\
\n\nНомер варианта ответа: '
        try:
            answer = int(input(menu))
            print('='*60)
        except:
            raise ValueError(f'\nЗначение ответа должно быть целым числом!\n')
        
        if not 1 <= answer <= 2:
            raise ValueError('\nВыбран неизвестный пункт!\n')

        return answer
