from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class Role:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f'{self.name}'


class RolesGenerator:
    class_type = Role
    file_path = '../TableData/Roles.csv'

    
    def __init__(self):
        self.container = list()
    

    def generate(self):
        self.container = [Role('гость'),
                          Role('читатель'),
                          Role('библиотекарь'),
                          Role('администратор')]


    def __str__(self):
        roles = ''.join([f'\t{str(role)}\n' for role in self.container])
        return f'Файл: {self.file_path!r}\nСгенерированные роли:\n{roles}\n'
