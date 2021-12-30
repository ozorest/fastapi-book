from pydantic import BaseModel, EmailStr, ValidationError, root_validator


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str
    @root_validator()
    def passwords_match(cls, values):
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            raise ValueError("Passwords don't match!")
        return values


try:
    user = UserRegistration(
        email = "thiago@ozorest.me",
        password = "abc",
        password_confirmation = "def"        
    )
    print(user)
except ValidationError as e:
    print(str(e))