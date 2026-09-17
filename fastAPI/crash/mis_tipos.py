from pydantic import BaseModel

class Data(BaseModel):
    name : str | None = "marco"
    age : int | None = 33
    idu : int

ob: Data = {
    "name": "marco",
    "age": 33,
    "idu": 7
}

print(ob.name)