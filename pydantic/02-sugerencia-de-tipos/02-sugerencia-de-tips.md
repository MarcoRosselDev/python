# Sugerencia de tipo  
La base sobre la que se contruye Pydantic.   
# que son las sugerencias de tipo?  
Las sugerencias de tipo le indican a Python (y a otros desarrolladores)  
que tipo de datos debe contener una variable:   
```python
name: str = "Dave"
age: int = 30
price: float = 19.99
is_active: bool = True
```
Los: str, :int, :float, y :bool son sugerencias de tipo.   
## Python no las impone

Aqui esta la clave:
    Python ignora las sugerencias de topo en tiempo de ejecucion.   
    Son solo documentacion:  

```python
age:int = "not a number" # Python permite esto
```

No hay un error.  
Python ejecuta este codigo sin problemas.   
Entonces, Por que usarlos ?   
## Beneficios de las sugerencias de topografia  
Las sugerencias de tipo te ofrececn tres ventajas:   
1. Documentacion: El codigo se vuelve autoexplicativo.
2. Soporte de IDE: autocompletado, deteccion de errores, refactorizacion.
3. Herramientas de validacion: Pydantic, mypy y otras.


Sin sugerencia de tipo:  
```python
def create_user(name, email, age):
    # De que tipo se supone que deben ser ?
    pass
```
Con sugerencias de tipo:   
```python
def create_user(name: str, email: str, age: int) -> dict:
    # Claro como el agua
    pass
```

# Tipos basicos

## Los cuatro tipos que usaras constantemente: 
```python
# Strings - texto
name: str = "Alice"
message: str = "Hello, world!"

# Integers - numeros enteros (N)
count: int = 42
user_id: int = 1001

# Floats - numeros punto decimal (Q)
price: float = 29.99
temperature: float = 98.6

# Booleans - true o false
is_active: bool = True
has_access: bool = False
```

Desde Python 3.9+, use tipos integrados en minusculas (list, dict, set, tuple).  
El codigo antiguo usa importaciones en mayusculas de typoing (List, Dict).   
Estos son equivalentes, pero ahora se prefieren las minusculas.   

# Valores opcionales

A veces, un valore puede no existir.   
Utilice Optional con la siguiente sintaxis:   
```python
from typing import Optional

# Esto significa lo mismo
middle_name: Optional[str] = None
middle_name: str | None = None
```
Utilizar opcional cuando un valor pueda ser None:  
```python
# User puede no tener un middle name
middle_name: str | None = None
middle_name: str | None = "James"

# Phone number es optional
phone: str | None = None
phone: str | None = "+1-555-0123"
```

# Tipos literales

cuando un valor debe ser una de opciones especificas:
```python
from typing import Literal

status: Literal["draft", "published", "archived"] = "draft"

# Only these three values are valid
status = "draft"      # OK
status = "published"  # OK
status = "pending"    # Type checkers will warn about this
```

ejemplo del mundo real:  
```python

from typing import Literal

log_level: Literal["debug", "info", "warning", "error"] = "info"
priority: Literal["low", "medium", "high"] = "medium"
status: Literal["pending", "approved", "rejected"] = "pending"

```

# Sugerencias sobre el tipo de funcion

Las sugerencias de tipo funcionan tanto en los parametros de funcion   
como en los valores de retorno:  
```python
def format_price(amount: float, currency: str = "USD") -> str:
    return f"{currency} {amount:.2f}"

def calculate_total(prices: list[float], tax_rate: float) -> float:
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)

def get_config(key: str) -> str | None:
    # Returns the config value if found, None if not
    pass
```
El simbolo -> str que aparece despues del parentesis indica el top de retorno.  
# Patrones de sugerencias de tipo comunes   
Estos son algunos patrones que veras constantemente en el codigo Python:   
```python
from typing import Optional, Literal

# Required string
name: str

# Optional string (can be None)
nickname: str | None = None

# String with default
country: str = "USA"

# List of items
items: list[str] = []

# Dictionary
metadata: dict[str, str] = {}

# Valores permitidos especificos
role: Literal["admin", "user", "guest"] = "user"
```

# Las sugerencias de topo no validan

Recuerda: Python ignora las sugerencias de tipo.  

Las sugerencias de tipo son solo sugerencias.   
No imponen nada.   

Aqui es donde entra en juego Pydantic.  
Pydantic lee las sugerencias de tipo y valida los datos   
comparandolos con ellos.   

# que sigue ?  
Ahora que ya entiendo las sugerencias de tipo, vamos a usarlas   
con Pydantic para crear mi primer modelo de datos validado.   
