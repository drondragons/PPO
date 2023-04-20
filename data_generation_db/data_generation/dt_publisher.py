from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Publisher:
    name: str = Validator(str, [Validator.exist_validator])
    country_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)