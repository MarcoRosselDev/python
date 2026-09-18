from pydantic import BaseModel

class Data(BaseModel):
    name : str | None = "marco"
    age : int | None = 33
    idu : int | None = None

""" ob = {
    "name": "marco",
    "age": 33,
    "idu": 7
}

e = Data(**ob)

print(e.age) """