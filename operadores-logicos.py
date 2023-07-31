""" operadores logicos """

""" And
Evalua si el operado izquierdo y el derecho son verdaderos.

x           y       x and y
True      True      True
True      False     False
False     True      False
False     False     False

"""
print("and")
boolAnd = (5 > 2) and (5 < 2)
print(boolAnd) # False

""" or

x           y       x and y
True      True      True
True      False     True
False     True      True
False     False     False

"""
print("or")
boolOr = (5 > 2) or (5 < 2)
print(boolOr) # True

""" not 
x       not x
True    False
False   True

"""

print("not")
boolNot = True
print(not(boolNot)) # False