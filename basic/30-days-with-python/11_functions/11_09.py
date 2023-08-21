""" 9. Declare a function named reverse_list. 
It takes an array as a parameter and it returns 
the reverse of the array (use loops). """

def reverse_list_filed(array):
    reverse = []
    for letter in array:
        reverse.insert(0, letter)
    StrA = "".join(reverse)
    return print(StrA)

reverse_list_filed('Hola') # aloH
reverse_list_filed('Me gusta python') # nohtyp atsug eM

# entendi mal el ejercicio!
# no resive un string si no un arreglo o array

""" example output:
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"] """

def reverse_list(array):
    mirror = []
    for item in array:
        mirror.insert(0, item)
    return print(mirror)

reverse_list([1, 2, 3, 4, 5]) # [5, 4, 3, 2, 1]
reverse_list(["A", "B", "C"]) # ['C', 'B', 'A']