from pydantic import BaseModel
""" tomorrow we're going to see more about this thing called pydantic
    I have already an Idea, but I would like to have a complete idea of this library
    to work with complete confidientiallity
 """


def working_with_pydantic( a:BaseModel):

    print(a)

    return "Hello world"

working_with_pydantic("Hi")

#print(BaseModel)