from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server: uvicorn getUsers:app --reload

@app.get("/usersJSON")
async def getUsers():
    return [
        {"name": "marco",
        "lastName": "rossel",
        "age": 30},
        {"name": "Eduardo",
        "lastName": "rossel",
        "age": 32}
    ]


class User(BaseModel):
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
@app.get("/userFromClass")
async def getUsersBaseModal():
    return users_list