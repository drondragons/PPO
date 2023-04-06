from dataclasses import dataclass
from AttributeValidator import Validator


@dataclass(frozen=True)
class Status:
    name: str = Validator(str, [Validator.exist_validator])


    def __str__(self):
        return f"{self.name}"


class StatusesGenerator:
    class_type = Status
    file_path = "../TableData/Status.csv"

    
    def __init__(self):
        self.container = list()
    

    def generate(self):
        self.container = [Status(name="добавлено"),
                          Status(name="списано"),
                          Status(name="забронировано"),
                          Status(name="выдано"),
                          Status(name="возвращено")]
