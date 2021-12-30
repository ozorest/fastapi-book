from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


try:
    user = User(
        email = "jdoe@jdoe.com",
        website = "https://www.jdoe.com"
    )
    print(user)
except ValidationError as e:
    print(str(e))