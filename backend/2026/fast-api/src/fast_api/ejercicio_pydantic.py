from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

opciones_de_genero = Literal["Ficción", "No Ficción", "Ciencia", "Historia", "Poesía"]
anio_actual = datetime.now().year

class Libro(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int = Field(ge=1450, le=anio_actual)
    # ver como se crean una lista de valores opcionales
    # similares a typescript en javascript
    # por ahora me esta gustando bastante
    genero: Optional[opciones_de_genero] = None
    #genero: Optional[str] = None , "Ficción", "No Ficción", "Ciencia", "Historia", "Poesía"
    disponible: bool = True

calculo = Libro(
    titulo="calculo 1", 
    autor="stewart",
    anio_publicacion=2012,
    disponible=False,
    genero="Ciencia"
    )

print(calculo)