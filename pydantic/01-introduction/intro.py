# pip install pydantic[email] para poder utilizar EmailStr
# EmailStr se instala aparte de pydantic
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    email: EmailStr
    age: int

# Valid data - works fine
user = User(id=1, email="dave@example.com", age=25)

# Invalid data - fails immediately with clear error
user = User(id=1, email="marco@something.com", age=30)