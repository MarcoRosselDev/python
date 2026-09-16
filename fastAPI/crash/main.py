from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name : str | None = "marco"
    age : int | None = 33

@app.get("/")
def read_root():
    return {"Hello": "Worldasdkfj"}

@app.post("/public")
def random_name(data:Data):
    print(data)
    return{ "mensaje":"Cuidado con los ovnis!",
           "data": data}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}