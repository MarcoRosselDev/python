# Validacion y Field()

## Mas alla de la comprobacion de tipos  

Pydantic valida los tipos, pero a menudo se necesita mas:  
    * Formato valido de correo
    * La edad debe ser positiva
    * El nombre debe tener entre 3 y 20 caracteres
    * El precio no puede ser negativo

La funcion Field() permite añadir estas restricciones.  

## La funcion Field() 

Importa Field desde Pydantic y usalo para agregar restricciones:  
```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0, le=120)
    email: str

user = User(name="Alice", age=30, email="alice@example.com")
```
Ahora name debe tener entre 1 y 100 caracteres,  
y age debe estar entre 1 y 120  

## restricciones de cadena

Controla la longitud y el formato de la cadena:
```python
from pydantic import BaseModel, Field

class UserProfile(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    bio: str = Field(max_length=500)
    website: str = Field(pattern=r"^https?://.*")

# Valid
profile = UserProfile(
    username="alice_dev",
    bio="Python developer",
    website="https://example.com"
)

# Invalid - username too short
profile = UserProfile(username="ab", bio="Hi", website="https://x.com")
# ValidationError: username must be at least 3 characters
```

Restricciones de cadena:  
* min_length - numero minimo de caracteres
* max_length - numero maximo de caracteres
* pattern - patron de expresion regular para coincidir

## Restricciones numericas

Rangos de numeros de control:  
```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    price: float = Field(gt=0)           # Mayor a 0
    quantity: int = Field(ge=0)          # Mayor o igual a 0
    discount: float = Field(ge=0, le=1)  # Entre 0 y 1

product = Product(
    name="Widget",
    price=29.99,
    quantity=100,
    discount=0.15
)
```

Restricciones numéricas:

* gt - Mayor que
* ge - Mayor o igual que
* lt - Menos de
* le - Menor o igual que

# Valores predeterminados con el campo  
Establezca valores predeterminados y, el mismo tiempo, agregue restricciones:  

```python
from pydantic import BaseModel, Field

class APIConfig(BaseModel):
    api_key: str
    model: str = Field(default="gpt-4")
    max_tokens: int = Field(default=1000, ge=1, le=4096)
    temperature: float = Field(default=0.7, ge=0, le=2)

# Only api_key required
config = APIConfig(api_key="sk-abc123")

print(config.model)        # gpt-4
print(config.max_tokens)   # 1000
print(config.temperature)  # 0.7
```

## Descripciones de campos
Agregar descripciones para la documentacion:  
```python
from pydantic import BaseModel, Field

class Order(BaseModel):
    order_id: str = Field(description="Unique order identifier")
    total: float = Field(gt=0, description="Order total in USD")
    items: int = Field(ge=1, description="Number of items in order")
```
Las descripciones aparecen en los esquemas JSON generados y en la documentacion de la API.

## Validadores personalizados (descripcion general 80/20)

A veces, las restricciones integradas no son suficientes.  
Pydantic admite validadores personalizados para la logica de negocio:  
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    
    @field_validator("username")
    def validate_username(cls, v):
        if " " in v:
            raise ValueError("Username cannot contain spaces")
        return v.lower()  # Normalize to lowercase

user = User(username="AliceSmith")
print(user.username)  # alicesmith
```
La funcion de validacion recibe cls (la clase, ya que aun no hay ninguna instancia durante la validacion)  
y v (el valor que se esta validando).  
Devuelve el valor para aceptarlo o genera una excepcion ValueError para rechazarlo.  

Los validadores presonalizados te permiten:  

* Agregar lógica de validación específica para el negocio   
* Transformar valores (como normalizarlos a minúsculas)   
* Validar elementos que las restricciones integradas no pueden manejar   

En la mayoria de los casos, las restricciones y los tipos integrados son suficientes.  
Utilice validadores personalizados solo cuando nevesite una logica de negocio especifica.  
## Ejemplo del mundo real  

Aqui tiene un modelo de formulario de pago:  
```python
from pydantic import BaseModel, Field

class PaymentForm(BaseModel):
    card_number: str = Field(min_length=16, max_length=16)
    expiry_month: int = Field(ge=1, le=12)
    expiry_year: int = Field(ge=2024)
    cvv: str = Field(min_length=3, max_length=4)
    amount: float = Field(gt=0, description="Amount in USD")
    currency: str = Field(default="USD", min_length=3, max_length=3)

payment = PaymentForm(
    card_number="1234567890123456",
    expiry_month=12,
    expiry_year=2025,
    cvv="123",
    amount=99.99
)
```

# PATRONES COMUNES

## Validacion de correo electronico  
```python
# pip install pydantic[email] o uv add pydantic[email]
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr  # Built-in email validation

```

## Validacion de URL 
```python
from pydantic import BaseModel, HttpUrl

class Link(BaseModel):
    url: HttpUrl  # Must be valid HTTP/HTTPS URL
```

## Listas restringidas
```python
from pydantic import BaseModel, Field

class Order(BaseModel):
    items: list[str] = Field(min_length=1)  # At least one item
```

## Generacion de esquema JSON

Pydantic puede generar esquemas JSON a partir de tus modulos.  
Esto es util para la documentacion de la API y la integracion con otras herramientas:  

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=1, description="User's full name")
    age: int = Field(ge=0, description="User's age in years")

print(User.model_json_schema())
```
Produccion:
```python
{
    'properties': {
        'name': {'description': "User's full name", 'minLength': 1, 'type': 'string'},
        'age': {'description': "User's age in years", 'minimum': 0, 'type': 'integer'}
    },
    'required': ['name', 'age'],
    'title': 'User',
    'type': 'object'
}
```

FastAPI utiliza esto para generar automaticamente la documentacion de la API.

### Que sigue?

Ya sabemos como validar campos individuales.  
Ahora, aprenderemos a manejar datos complejos con modelos animdados.  