from datetime import datetime
from pydantic import BaseModel

class Author(BaseModel):
    name: str=None
    id:int
    age:int
    fecha: datetime | None

tst_data = {
    'id':1,
    'name': 'marco',
    'age': 33,
    'fecha': '2019-06-01 12:22'
}

usuario = Author(**tst_data)

print(usuario.age) # 33
print(usuario.model_dump())