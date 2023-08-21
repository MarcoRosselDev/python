""" 9. Declare a function named reverse_list. 
It takes an array as a parameter and it returns 
the reverse of the array (use loops). """

def reverse_list(array):
    reverse = []
    for letter in array:
        reverse.insert(0, letter)
    StrA = "".join(reverse)
    return print(StrA)

reverse_list('Hola') # aloH
reverse_list('Me gusta python') # nohtyp atsug eM