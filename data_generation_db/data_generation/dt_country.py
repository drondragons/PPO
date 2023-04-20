from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Country:
    name: str = Validator(str, [Validator.exist_validator])