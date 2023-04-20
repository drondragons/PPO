from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class LiteraryWorkGenre:
    literary_work_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    genre_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)