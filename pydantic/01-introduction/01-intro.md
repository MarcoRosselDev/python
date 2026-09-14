# Introduccion

Pydantic incorpora la validacion de datos en tiempo de ejecucion  
a Python mediante sugerencias de tipo.

## El problema de Python

Python es de tipado dinamico.  
Esto significa que puedes hacer lo siguiente   
```python
age = 33
age = "ahora es un texto"
age = ["25", True, None]
```

No hay errores.
A Python le vale madres.  

Esta flexibilidad es ideal para scripts rapidos.  
Pero se convierte en una pesadilla cuando se desarrollan aplicaciones reales,   
especialemente al trabajar con datos externos.   

## Cuando las cosas salen mal 

Imagina que estas creando una API que recibe datos de usuario:  
```python
def create_user(data):
    user_id = data["id"]
    email = data["email"]
    age = data["age"]
    
    # Later in your code...
    birth_year = 2025 - age  # What if age is "25" instead of 25?
```
Tu API recibe JSON del mundo exterior. Esperas:
```
{"id": 1, "email": "dave@example.com", "age": 25}
```
pero la API envia:
```
{"id": 1, "email": null, "age": "unknown"}
```
Tu codigo falla.

## El impacto en el mundo real
En cualquier aplicacion, constantemente trabajas con:  

* Respuestas de la API
* Entrada del Usuario
* Configuracion
* Registro de la base de datos

Sin validacion, los errores permanecen ocultos hasta que llegan a produccion.  
Con Pydantic, salen a la luz de inmediato.  

## Lo que hace Pydantic
Pydantic valida los datos en tiempo de ejecucion.  
Usted define como deben ser sus datos y Pydantic se asegura de que coincidan:  
```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    age: int

# Valid data - works fine
user = User(id=1, email="dave@example.com", age=25)

# Invalid data - fails immediately with clear error
user = User(id=1, email=None, age="unknown")
```
Cuando falla la validacion, recibes un mensaje de error claro   
que le indicara exactamente que salio mal:  
```python
2 validation errors for User
email
  Input should be a valid string
age
  Input should be a valid integer, unable to parse string as an integer
```
El problema se soluciona de raiz.   
## Pydantic en el ecosistema de Python

Pydantic esta en todas partes:  
* FastAPI
* Django Ninja
* SQLModel
* la mayoria de frameworks modernos se basan en pydantic internamente

Aprender Pydantic consiste en escribir Python fiable y con seguridad de tips.  

## Instalacion

Instala Pydantic en tu proyecto con cualquiera de las siguientes opciones:   
```terminal
pip install pydantic
```
```terminal
uv add pydantic
```

## ¿ Por que apreder Pydantic ? 

Junto con los fundamentos de Python, Pydantic es una de las bibliotecas  
mas importantes que hay que aprender, especialmente en la era de la  
programacion con agentes.

* Aplicaciones mas robustas
* Los agentes de IA comprenden mejor tu codigo
* Necesitas una salida estructurada para sistmas basados en agentes?
* Lo encontraras por todas partes

## Que sigue ?

Antes de profundizar en Pydantic, es necesario comprender las  
sugerencias de tipos.   
Son la base sobre la que se construye Pydantic.  