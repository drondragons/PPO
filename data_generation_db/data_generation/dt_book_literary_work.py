from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class BookLiteraryWork:
    book_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    literary_work_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)