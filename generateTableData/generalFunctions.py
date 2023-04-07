from os import path, makedirs


class GeneralFunctions:
    @staticmethod
    def is_existFile(file_path):
        return path.exists(file_path)


    @staticmethod
    def createDir(dir_path):
        try:
            makedirs(dir_path)

        except:
            raise OSError(f'\nНе удалось создать папку {dir_path!r}!\n\
Проверьте название папки или права доступа!\n')


    @staticmethod
    def chooseMenuPoint(file_path):
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
