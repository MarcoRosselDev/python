""" Sentencia condicional

Intruccion o un grupo de intrucciones cuya
ejecucion depende del valor de una condicion
booleana.

"""

if (1 > 0): print('hola')

""" else (si no)

si la condicion es falsa se ejecuta else

if (condicion): 
    ejecutar si es verdad
else:
    ejecutar si no es verdad
"""

valor = 10

if valor > 20:
    print("verdad")
else:
    print("false")

""" elif

se pueden aplicar mas condicionales con elif
"""

if valor > 20:
    print("mayor a 20")
elif valor > 30:
    print("mayor a 30")
elif valor > 40:
    print("mayor a 40")
else:
    print("menor a 20")