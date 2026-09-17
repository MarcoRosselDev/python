from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from data_de_practica import datitos
from mis_tipos import Data
from encontrar_publicacion import encontrar_publicacion

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": datitos}

@app.post("/public", status_code=status.HTTP_201_CREATED) # actualizar status, porque por defecto es 200 y eso esta mal
def random_name(data: Data):
    print(data)

    datitos.append(data)

    return{ 
        "mensaje": "publicacion exitosa !"
        }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):

    publicacion = encontrar_publicacion(item_id)
    if not publicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"el item {item_id} no se encontro mi amiguito !"
            )
    
    return {"item_id": item_id, "q": q}

















""" 
    if not data:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Error en los datos my friend")
        return {"mensaje": ""}
 """