from validation import Validator
from dataclasses import dataclass


regex_users_initials = "^[а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+ [а-яА-ЯёЁ\-]+$"
regex_phone_number = "^8\d{10}$"


@dataclass(frozen=True)
class User:
      login: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 8, 50, "[^\~\-_a-zA-Z0-9]")
      email: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 8, 50, "[^\~\-\.\@_a-zA-Z0-9]")
      initials: str = Validator(str, [Validator.exist_validator, Validator.match_validator, Validator.length_validator], 1, 50, regex_users_initials)
      role_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
      phone_number: str = Validator(str, [Validator.exist_validator, Validator.match_validator, Validator.length_validator], 11, 11, regex_phone_number)
      password: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 8, 20, "[^\~\-_a-zA-Z0-9]")
      actuality: bool = Validator(bool)
      birth_date: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 5, 10, "[^\d\.]")