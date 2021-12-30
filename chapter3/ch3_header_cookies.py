from fastapi import FastAPI, Header, Cookie
from typing import Optional

app = FastAPI()

@app.get("/")
async def get_header(hello: str = Header(...)):
    return {"hello": hello}

@app.get("/user-agent")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

@app.get("/cookie")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}