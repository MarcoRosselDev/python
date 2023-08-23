# 1. Writ a function which generates a six digit/character random_user_id.

""" example output:
print(random_user_id());
'1ee33d' """

from random import random, randint

# para no llamar el modulo string mejor tomo las letras y numeros de un string
str_letters = 'abcdefghijklmnopqrstuvwxyz'
str_letters_mayusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_digits = '0123456789'

def list_creator(string):
    list_returned = []
    for letter in string:
        list_returned.append(letter)
    return list_returned

# creamos listas de letras mayusculas, minusculas y numeros para llamarlos de forma aleatoria
letters_list = list_creator(str_letters)
numbers_list = list_creator(str_digits)
letters_list_mayusc = list_creator(str_letters_mayusc)



def random_user_id():
    print('break')