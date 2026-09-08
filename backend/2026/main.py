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

def bucle_for_diccionario ():
    my_dicc = {'name': 'marco', 'age': 33, 'pareja': True}

    for clave, valor in my_dicc.items():
        print(clave, valor)
    # name marco
    # age 33
    # pareja True

def bucle_while():
    num = 0

    while num < 25:
        print(num)
        num+=3
    # 0
    # 3
    # 6
    # 9
    # 12
    # 15
    # 18
    # 21
    # 24

def fibonacci (n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(8))

arr = []

for num in range(13):
    arr.append(fibonacci(num))

print(arr) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]