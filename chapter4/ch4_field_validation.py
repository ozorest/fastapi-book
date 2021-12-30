from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)


try:
    p = Person(
        first_name="Jonh",
        last_name="Doe",
        age=25        
    )
    print(p)
except ValidationError as e:
    print(str(e))