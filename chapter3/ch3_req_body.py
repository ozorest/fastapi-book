from fastapi import FastAPI, Body
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name: str    

app = FastAPI()

@app.post("/users1")
async def create_user(name: str = Body(...), age: int = Body(...)):
    return {
        "name": name,
        "age": age
    }

@app.post("/users2")
async def create_user(user: User):
    return user

@app.post("/users3")
async def create_user(user: User, company: Company):
    return {"user": user, "company": company}

@app.post("/users4")
async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
    return {"user": user, "priority": priority}