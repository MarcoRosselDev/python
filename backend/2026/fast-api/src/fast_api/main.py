from fastapi import FastAPI, Body
from pydantic import BaseModel
#from fastapi import Body

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class Body_Post(BaseModel):
    title: str
    content: str
    age: int

@app.post("/post/new-item")
def post_new_item(body:Body_Post):
    print(body.content, body.title, body.age)
    return {"msg":"Contenido publicado exitosamente!"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/post")
def extract_body(body:dict = Body(...)):
    """ if we past to the body :
    {
        "nombre": "marco",
        "age": 33
    }
    we get:

    {'nombre': 'marco', 'age': 33} 
    if we print body in the console
    """
    print(body)
    return {"mess": "info publicada"}

""" @app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id} """