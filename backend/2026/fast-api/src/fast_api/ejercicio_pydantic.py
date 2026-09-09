from pydantic import BaseModel, Field
from typing import Optional
import datetime

anio_actual = datetime.now().year

class Libro(BaseModel):
    titulo: str
    autor: str
    anio_publicacion: int = Field(ge=1450, le=anio_actual)
    # ver como se crean una lista de valores opcionales
    # similares a typescript en javascript
    # por ahora me esta gustando bastante
    genero: Optional[str] = None , "Ficción", "No Ficción", "Ciencia", "Historia", "Poesía"