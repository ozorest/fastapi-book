from fastapi import FastAPI, Response, status
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    nb_views: int

app = FastAPI()

posts = {
    1: Post(title="Ola", nb_views=100)
}

@app.get("/header")
async def custom_header(response: Response):
    response.headers["Custom-Header"] = "Custom-Header-Value"
    return {"fastapi": "rocks"}

@app.get("/cookie")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"fastapi": "rocks"}

@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
        posts[id] = post
        return posts[id]