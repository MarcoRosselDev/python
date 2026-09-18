from fastapi import FastAPI, status, HTTPException
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
    datitos.append(data.model_dump())
    return{"mensaje": "publicacion exitosa !"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):

    publicacion = encontrar_publicacion(item_id)

    if not publicacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"el item {item_id} no se encontro mi amiguito !"
            )
    
    return {
        "item_id": item_id, 
        "q": q,
        "data": publicacion
        }

def find_index(id:int):
    for index, post in enumerate(datitos):
        if post["idu"] == id:
            return index

@app.delete("/items/{item_id}")
def delete_post(item_id: int):
    # buscar el index si existe en la data
    index = find_index(item_id)
    if index:
        # eliminar el item con el index encontrado
        datitos.pop(index)
        # retornar una exception
        return HTTPException(
            status_code=status.HTTP_410_GONE,
            detail=f"se elimino exitosamente el item con el id {item_id} !"
            )
    else:
        # retornar una exception
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"no se encontro el item {item_id}"
        )

@app.put("/items/{item_id}")
def put_item(item_id:int, contenido: Data):
    index = find_index(item_id)
    if index == None:
        # de lo contrario, buscar le item en datitos y actualizarlo
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontro el indice {item_id}, no se actualizo ni madres !"
            )

    contenido_nuevo = contenido.model_dump()
    print(contenido_nuevo)
    contenido_nuevo["idu"] = item_id
    print(contenido_nuevo)
    datitos[index] = contenido_nuevo

    return{"data": contenido_nuevo, "id": item_id}




""" from data_de_practica import datitos   
def find_index(id:int):
    for index, post in enumerate(datitos):
        if post["idu"] == id:
            return index

i = find_index(1)
print(i, type(i)) """









""" 
    if not data:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Error en los datos my friend")
        return {"mensaje": ""}
 """