from validation import Validator
from dataclasses import dataclass


@dataclass(frozen=True)
class BookRecord:
    user_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    book_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    book_status_id: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    book_amount: int = Validator(int, [Validator.exist_validator, Validator.interval_validator], 1)
    date: str = Validator(str, [Validator.exist_validator, Validator.symbols_validator, Validator.length_validator], 11, 19, '[^\:\d\. ]')