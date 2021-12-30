from enum import Enum
from fastapi import FastAPI, Path

class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

app = FastAPI()

@app.get("/users/{type}/{id}/")
async def get_user(type: UserType, id: int = Path(..., ge=1)):
    return {
        "type": type,
        "id": id
    }

@app.get("/license-plates/{license}")
async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}
