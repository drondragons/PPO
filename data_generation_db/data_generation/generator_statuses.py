from dt_status import Status
from generator_abstract import DataGenerator


class StatusesGenerator(DataGenerator):
    def __init__(self, path='../TableData/Statuses.csv', class_type=Status):
        super().__init__(path, class_type)
    
    
    def generate_statuses(self):
        return [Status(name='добавлено'),
                Status(name='списано'),
                Status(name='забронировано'),
                Status(name='выдано'),
                Status(name='возвращено'),
                Status(name='отменено бронирование')]
    

    def generate(self, container=list()):
        self.container = self.generate_statuses()