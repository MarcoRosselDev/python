from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/url")
async def url():
    return {"return_json":"mesaje from /url"}


@app.get("/users")
async def getUsers():
    return { "futuros usuarios"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
