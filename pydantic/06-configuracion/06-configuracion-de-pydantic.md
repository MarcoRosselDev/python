# Configuracion de Pydntic

Configuracion segura en cuanto a tipos a partir de variables de entorno.  

## El problema con las variables de entorno  

Las variables de entorno son cadenas de caracteres.  
Siempre:  
```python
import os

api_key = os.getenv("API_KEY")           # str | None
max_connections = os.getenv("MAX_CONNECTIONS")  # str | None - not an int!
debug_mode = os.getenv("DEBUG")          # str | None - not a bool!
```
Tienes que hacerlo manualmente:  

* Comprobar si existen valores   
* Tipos de conversion  
* Validar valores  
* Gestionar valores predeterminados  

Esto provoca errores.  
Pydantic Settings soluciona este problema.  

## INSTALACION

Pydantic Settings es un paquete independiente.  
Agregalo a tu proyecto:  

```terminal
uv add pydantic-settings
```

## Tu primera clase de configuracion  

Crea una clase de configuracion que lea las variables de entorno:  

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: str
    max_connections: int = 100
    debug: bool = False

# Reads from environment variables automatically
settings = Settings()

print(settings.api_key)           # From API_KEY env var
print(settings.max_connections)   # From MAX_CONNECTIONS or default 100
print(settings.debug)             # From DEBUG or default False
```

Configura las variables de entorno en tu shell:  

```python
export API_KEY="sk-abc123"
export MAX_CONNECTIONS="200"
export DEBUG="true"
```

Luego, ejecuta tu codigo Python.  
Python lo lee y lo valida automaticamente.  

## Como funciona

La configuracion de Pydantic asigna nombres de campos a variables de entorno:  

| Nombre del campo | Varialbe de entorno |
|------------------|---------------------|
| api_key          | API_KEY             |
| max_connections  | MAX_CONNECTIONS     |
| database_url     | DATABASE_URL        |

Los nobmres de los campos se convierten a mayusculas para la busqueda en variables de entorno.  

## Conversion de tipo  

Pydantic Settings gestiona la conversion de tipos automaticamente:  

```python  
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int              # "8080" -> 8080
    debug: bool            # "true" -> True
    rate_limit: float      # "1.5" -> 1.5
    allowed_hosts: list[str]  # "host1,host2" -> ["host1", "host2"]
```

Valores booleanos aceptados: true, false, 1, 0, yes, no, on, off  

## Cargando desde archivos .env

Almacenar las variables de entorno en archivo .env :

```env
# .env
API_KEY=sk-abc123
DATABASE_URL=postgresql://localhost/mydb
DEBUG=true
MAX_CONNECTIONS=200
```

Configura tus ajustes para leer desde alli:  

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    api_key: str
    database_url: str
    debug: bool = False
    max_connections: int = 100

settings = Settings()
print(settings.api_key)  # sk-abc123
```

model_config le indica a pydantic donde encontrar el .env  

## prefijo de variable de entorno  

Agregue un prefijo para evitar conflicto de nombres:  

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="MYAPP_")
    
    api_key: str
    debug: bool = False

# Now reads from MYAPP_API_KEY and MYAPP_DEBUG
settings = Settings()
```

Tu archivo .env :  
```env
MYAPP_API_KEY=sk-abc123
MYAPP_DEBUG=true
```

# Manejo de secretos  

Uso de SecretStr para valroes sensibles:  
```python
from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_key: SecretStr
    database_password: SecretStr

settings = Settings()

# Secrets are hidden when printed
print(settings.api_key)  # **********

# Access the actual value when needed
actual_key = settings.api_key.get_secret_value()

```