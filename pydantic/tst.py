from pydantic import BaseModel

class User(BaseModel):
    name:str
    last_name: str
    age: int
    is_gay: bool

try:
    eduardo = User(
        age=35, 
        name="Eduardo", 
        last_name="Rossel")
    print(eduardo.name)
except Exception as e:
    print(e)

    """ 
    1 validation error for User
    is_gay
    Field required [type=missing, input_value={'age': 35, 'name': 'Edua..., 'last_name': 'Rossel'}, input_type=dict]
        For further information visit https://errors.pydantic.dev/2.13/v/missing
    """