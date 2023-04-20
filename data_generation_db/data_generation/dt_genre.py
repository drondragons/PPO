from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class Genre:
    title: str = Validator(str, [Validator.exist_validator])
    description: str = Validator(str, [Validator.exist_validator])