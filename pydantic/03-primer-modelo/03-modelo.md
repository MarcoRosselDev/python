# Tu primer modelo

## Que es un modelo ?

Un modelo Pydantic es una clase que define la estructura de tus datos.   
Escpecifica que campos existen y que tipo deben tener:   
```python
from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    age:int

Este modelo dice: 
```
"Un usuario tiene un nombre (cadena de caracter),
un correo (cadena de caracter) y   
una edad (numero entero)".   

# Clases de datos frente a Pydantic   

Python cuenta con clases de datos integradas para definir estructuras de datos:   
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age="not a number")
print(user.age)  # "not a number" - no validation!
```

El decorador @dataclass genera un metodo __init__ a partir de las sugerencias   
de tipo.   
Sin el, se produce un error TypeError: User()
    takes no arguments   
Porque una clase siempre con anotaciones no acepta argumentos en el constructor.  

Las clases de datos proporcionan una sintaxis limpia para los contenedores de datos,  
pero no validan nada.   
Las sugerencias de tipo son solo documentacion.   

Los modelos de Pydantic se parecen, pero en ralidad imponen los tipos:
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age="not a number")
# ValidationError: Input should be a valid integer
```
Para la mayoria de los proyectos, basta con usar Pydantic.  
Obtendra validacion, serializacion y generacion de esquemas JSON   
con una sobrecarga minima.  
Pydantic v2 es tan rapido que la diferencia de rendimiento rar vez importa.   

# Creacion de instancias  
Crea una instancia del modelo pasandole datos:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

# Create a user
user = User(name="Alice", email="alice@example.com", age=30)

print(user.name)   # Alice
print(user.email)  # alice@example.com
print(user.age)    # 30
```
Pydantic valida los datos al crear la instancia.  
Los datos no validos generan un error inmediatamente.   

# Validacion en accion

Intenta pasar datos no validos:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

# Esto correra un validation error
user = User(name="Alice", email="alice@example.com", age="thirty")
```
Error:
```terminal
ValidationError: 1 validation error for User
age
  Input should be a valid integer, unable to parse string as an integer
```
El error te indica exactamente que fallo y donde.   

# Creacion de tipos automatica

Pydantic es inteligente en cuanto a la conversion de tipos.    
Convierte automaticamente los tipos ccompatibles:   
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# String "25" se convierte a integer 25
user = User(name="Alice", age="25")
print(user.age)        # 25
print(type(user.age))  # <class 'int'>
```
Esto resulta util al trabajar con datos de formularios de API donde los numeros  
se presentan como cadenas de texto.   

# Campos obligatorios frente a campos opcionales  

Los campos sin valores predeterminados son obligatorios:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str              # Obligatorio
    email: str             # Obligatorio
    age: int | None = None # Optional (tiene valor por defecto = None)

# Funciona - age es optional
user = User(name="Alice", email="alice@example.com")
print(user.age)  # None

# Tambien funciona - ingresa age
user = User(name="Bob", email="bob@example.com", age=25)
print(user.age)  # 25
```

# Valores predeterminados

Establezca valores predeterminados para los campos que suelen tener un valor comun:  

```python
from pydantic import BaseModel

class APIConfig(BaseModel):
    api_key: str
    model: str = "gpt-4"
    max_tokens: int = 1000
    temperature: float = 0.7

# Only api_key is required
config = APIConfig(api_key="sk-abc123")

print(config.model)       # gpt-4
print(config.max_tokens)  # 1000
```

# Convertir a diccionario  
Se utiliza model_dump() para convertir un modelo en un diccionario:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age=30)

# Convert to dict
user_dict = user.model_dump()
print(user_dict)
# {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}
```
Esto es util cuando necesitas :
    * Enviar datos a una API
    * Almacenar en una base de datos
    * Serializar a JSON

# Convertir a JSON  
Se utiliza model_dump_json() para obtener una cadena JSON:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

user = User(name="Alice", email="alice@example.com", age=30)

# Convert to JSON string
json_string = user.model_dump_json()
print(json_string)
# {"name":"Alice","email":"alice@example.com","age":30}
```

# Creacion a partir de un diccionario  
Dos maneras de crear un modelo a partir de un diccionario:  
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

# Data from an API response
data = {"name": "Alice", "email": "alice@example.com", "age": 30}

# Option 1: Unpack the dict (simple, common)
user = User(**data)

# Option 2: Use model_validate (explicit, more options)
user = User.model_validate(data)
```
Ambos validan los datos.  
**data uselo para casos sencillos.  
model_validate() uselo cuando necesite opciones como strict=True.  

Este es el patron que utilizaras con mayor frecuencia:  
    recibir datos como un diccionario (desde una API, base de datos o archivo)  
    y validarlos para convertirlos en un modelo.  

# Modelos como sugerencias de tipo 

Los modelos Pydantic funcionan como sugerencias de tipo en tus funciones.  
Esto te proporciona autocompletado y comprobacion de tipos en el IDE.  

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

def greet_user(user: User) -> str:
    return f"Hello, {user.name}!"

def load_user(data: dict) -> User:
    return User.model_validate(data)

# IDE knows 'user' is a User, autocomplete works
user = load_user({"name": "Alice", "email": "alice@example.com"})
message = greet_user(user)
print(message)  # Hello, Alice!
```
Esto hace que tu codigo se autodocumente.  
Cuando veas esto user:User en la firma de una funcion,
sabras exactamente que datos paearle.  

# Ejemplo del mundo real

Aqui un modelo para gestionar las respuestas de la API:
```python
from pydantic import BaseModel

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    humidity: int
    description: str

# Simulating API response
api_data = {
    "city": "Amsterdam",
    "temperature": 18.5,
    "humidity": 75,
    "description": "Partly cloudy"
}

# Validate and parse
weather = WeatherResponse.model_validate(api_data)

print(f"Weather in {weather.city}: {weather.temperature}°C")
print(f"Humidity: {weather.humidity}%")
print(f"Conditions: {weather.description}")
```

# Errores comunes 

## Olvidar las sugerencias de tipo
```python
# Wrong - no type hints
class User(BaseModel):
    name
    email

# Right - always include type hints
class User(BaseModel):
    name: str
    email: str
```

## Valores predeterminados modificados

En las clases Python normales, = [] esto es peligroso  
porque todas las instancias comparten la misma lista.  
Pydantic lo maneja correctamente y crea una nueva lista para cada instancia:  

```python
from pydantic import BaseModel

class User(BaseModel):
    tags: list[str] = []  # Safe in Pydantic - each instance gets its own list

user1 = User()
user2 = User()
user1.tags.append("python")
print(user2.tags)  # [] - not affected
```

Tambien puedes usar Field(default_factory=list)  
si prefieres ser explicito, pero no es obligatorio en Pydantic.  

# Modo estricto

Por defecto, Pydantic convierte tipos compatibles (como "23" a 23).  
Si desea deshablilitar esto y requiere tipos exactos,  
utilice el modo esticot:  

```python
from pydantic import BaseModel, ConfigDict

class StrictUser(BaseModel):
    model_config = ConfigDict(strict=True)
    
    name: str
    age: int

# This will fail - no coercion allowed
user = StrictUser(name="Alice", age="25")
# ValidationError: Input should be a valid integer
```

model_config es un nombre de atributo especial de Pydantic busca.  
ConfigDict contiene opciones de configuracion para el modelo.  
Para la mayoria de los casos de uso, el modo relajado predeterminado  
es el que necesitas.  

# Que sigue ?  
Ahora ya sabes como crear modelos basicos.  
Ahora , aprenderemos a añadir reglas de validacion y restricciones a tus campos.  