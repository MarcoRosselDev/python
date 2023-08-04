from typing import Union

from fastapi import FastAPI

app = FastAPI()

class User():
    name: str
    lastName: str
    age: int
    url: str 

users_list = [
    User(name="marco", lastName="rossel",age=30 ,url="www.mrossel.com"),
    User(name="eduardo", lastName="rossel",age=32 ,url="www.erossel.com"),
    User(name="juan", lastName="medina",age=35 ,url="www.jmedina.com"),
    User(name="jayson", lastName="ruminot",age=14 ,url="www.jsonRuminot.com"),
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/url")
async def url():
    return {"return_json":"mesaje from /url"}


@app.get("/users")
async def getUsers():
    return { users_list }
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}