from dt_role import Role
from generator_abstract import DataGenerator


class RolesGenerator(DataGenerator):
    def __init__(self, path='../TableData/Roles.csv', class_type=Role):
        super().__init__(path, class_type)
        
    
    def generate_roles(self):
        return [Role('гость'),
                Role('читатель'),
                Role('библиотекарь'),
                Role('администратор')]
        
        
    def generate(self, container=list()):
        self.container = self.generate_roles()
