from datetime import date

from pydantic import BaseModel, validator
from pydantic.error_wrappers import ValidationError


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date
    @validator("birthdate")
    def valid_birthdate(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return v


try:
    person = Person(
        first_name = "Thiago",
        last_name = "Ozores",
        birthdate = "1984-01-01"
    )
    print(person)
except ValidationError as e:
    print(str(e))