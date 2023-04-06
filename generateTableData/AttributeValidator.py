from re import findall, match

class Validator:
    def __init__(self, class_type, validators=(), minimum=0, maximum=0, regex=""):
        self.regex = regex
        self.minimum = minimum
        self.maximum = maximum
        self.class_type = class_type
        self.validators = validators


    def __set_name__(self, owner, name):
        self.name = name


    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not isinstance(value, self.class_type):
            raise TypeError(f"\nЗначение атрибута {self.name!r}={value!r}\
 должно принадлежать {self.class_type!r}, а не {type(value)!r}!\n")
        
        for validator in self.validators:
            validator(self.name, value, self.minimum, self.maximum, self.regex)
        instance.__dict__[self.name] = value


    @staticmethod
    def exist_validator(name, value, *option):
        if not value:
            raise ValueError(f"\nЗначение атрибута {name!r}={value!r}\
 не должно быть пустым!\n")


    @staticmethod
    def symbols_validator(name, value, *option):
        if option[2]:
            forbidden_symbols = option[2]
            symbols = set(findall(forbidden_symbols, value))
            if symbols:
                raise ValueError(f"\nЗначение атрибута {name!r}={value!r}\
 не должно содержать {symbols!r}!\n")


    @staticmethod
    def match_validator(name, value, *option):
        if option[2]:
            pattern = option[2]
            if not match(pattern, value):
                raise ValueError(f"\nЗначение атрибута {name!r}={value!r}\
 должно удовлетворять паттерну {pattern!r}!\n")


    @staticmethod
    def length_validator(name, value, *option): 
        if option[0] and option[0] > len(value):
            raise ValueError(f"\nЗначение атрибута {name!r}={value!r}\
 должно содержать минимум {option[0]!r} допустимых символов!\n")

        if option[1] and option[1] < len(value):
            raise ValueError(f"\nЗначение атрибута {name!r}={value!r}\
 должно содержать максимум {option[1]!r} допустимых символов!\n")
