# 1. Importamos lo necesario
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

# 2. Definimos nuestro primer modelo
class Usuario(BaseModel):
    # Los campos se definen con anotaciones de tipo
    id: int
    nombre: str
    email: str
    # Campo opcional. Si no se provee, su valor será None
    edad: Optional[int] = None
    # Campo con validaciones adicionales usando Field()
    pais: str = Field(default="Desconocido", min_length=2, max_length=50)

# 3. Creamos una instancia válida del modelo
usuario_valido = Usuario(
    id=1,
    nombre="Ana García",
    email="ana@email.com",
    edad=30,
    pais="México"
)

print("--- Usuario Válido ---")
print(usuario_valido)
print(f"ID: {usuario_valido.id}")
print(f"Nombre: {usuario_valido.nombre}")
print(f"Email: {usuario_valido.email}")
print(f"Edad: {usuario_valido.edad}")
print(f"País: {usuario_valido.pais}")

# 4. Intentamos crear una instancia inválida (con errores)
print("\n--- Intentando crear usuario inválido ---")
try:
    usuario_invalido = Usuario(
        id="no soy un número",  # Error: debe ser un int
        nombre="",               # Podría pasar, pero queremos validar
        email="correo-invalido", # Error: no es un email válido (aunque Pydantic no lo valida por defecto)
        # edad no se proporciona, es opcional, así que está bien
        pais="X"                 # Error: min_length es 2
    )
except ValidationError as e:
    # Pydantic lanza una ValidationError con todos los detalles
    print("¡Error de validación!")
    print(e)


    """ output 
    --- Usuario Válido ---
    id=1 nombre='Ana García' email='ana@email.com' edad=30 pais='México'
    ID: 1
    Nombre: Ana García
    Email: ana@email.com
    Edad: 30
    País: México

    --- Intentando crear usuario inválido ---
    ¡Error de validación!
    2 validation errors for Usuario
    id
    Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='no soy un número', input_type=str]
        For further information visit https://errors.pydantic.dev/2.13/v/int_parsing
    pais
    String should have at least 2 characters [type=string_too_short, input_value='X', input_type=str]
        For further information visit https://errors.pydantic.dev/2.13/v/string_too_short
    """