edades = {'gino': 35, 'nora': 45}
#print(edades['gino']) # 35
#print(edades.get("gino")) # 35


def if_test_statement () :
    value = int(input("dime un numero entero: "))

    if value < 0:
        print("tu numero es negativo")
    elif value == 0:
        print("tu numero es cero")
    else:
        print("tu numero es positivo")

def bucle_for_statement() :
    cuantity = 5
    for numero in range(1, cuantity + 1):
        print(numero)
    """ 
    1
    2
    3
    4
    5
    """
def bucle_for_string () :
    for caracter in 'string':
        print(caracter)

    # s
    # t
    # r
    # i
    # n
    # g

my_dicc = {'name': 'marco', 'age': 33, 'pareja': True}

for clave, valor in my_dicc.items():
    print(clave, valor)
# name marco
# age 33
# pareja True