from mis_tipos import Data

lista_de_datos : list[Data] = [
    Data(name="marco", age=33, idu=1),
    Data(name="mane", age=18, idu=2),
    Data(name="papita", age=35, idu=3),
]

datitos = []

for item in lista_de_datos:
    x = item.model_dump()
    datitos.append(x)
