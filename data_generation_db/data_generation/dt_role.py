from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class Role:
    name: str = Validator(str, [Validator.exist_validator])