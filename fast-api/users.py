from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"home": "hello world"}

@app.get("/users")
async def users():
    return {"json users": "json de users /users"}