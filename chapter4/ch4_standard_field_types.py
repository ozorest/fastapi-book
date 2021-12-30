from datetime import date
from enum import Enum
from typing import List

from pydantic import BaseModel, ValidationError


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address


try:
    p = Person(
        first_name="Jonh",
        last_name="Doe",
        # gender="INVALID_VALUE", # cause validation error
        gender=Gender.MALE,
        birthdate="1991-01-01",
        # birthdate="1991-02-31", # cause validation error
        interests=["travel", "sports"],
        address={
            "street_address": "Rua Pedro de Toledo 2302",
            "postal_code": "13333320",
            "city": "Indaiatuba",
            "country": "Brazil"
        }
    )
    print(p)
except ValidationError as e:
    print(str(e))
