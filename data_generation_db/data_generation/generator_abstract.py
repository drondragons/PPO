from abc import ABC, abstractmethod


class DataGenerator(ABC):
    def __init__(self, path, class_type):
        self.path = path
        self.container: list()
        self.class_type = class_type
        
    
    @abstractmethod
    def generate(self, container=list()):
        pass