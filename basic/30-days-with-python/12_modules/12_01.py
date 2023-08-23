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
print('letters_min_list = ', letters_list)
numbers_list = list_creator(str_digits)
print('numbers_list = ', numbers_list)
letters_list_mayusc = list_creator(str_letters_mayusc)
print('letter_may_list = ', letters_list_mayusc)



def random_user_id():
    random_leng_id = randint(6, 10) # largo aleatoria entre 6 y 10 digitos
    id = '' # string donde agregar los valores en cada iteracion
    for iteration in range(0, random_leng_id):
        random_type_list = randint(0, 2)
        if random_type_list == 0:   # si es 0 iteramos aleatoriamente por la lista de letras minusculas
            random_letters_list_index = randint(0, len(letters_list) - 1 )
            id = id + letters_list[random_letters_list_index]
        elif random_type_list == 1:     # si es 1 iteramos aleatoriamente por la lista de numeros
            random_numbers_list_index = randint(0, len(numbers_list) - 1)
            id = id + numbers_list[random_numbers_list_index]
        elif random_type_list == 2:     # si es 2 iteramos aleatoriamente por la lista de letras mayusculas
            random_letters_list_mayusc_index = randint(0, len(letters_list_mayusc) - 1 )
            id = id + letters_list_mayusc[random_letters_list_mayusc_index]
        else:
            id = id + ''
    return print(id)

random_user_id() # Cw9aYf       GU6N3Q
random_user_id() # 30BCNQk      U6L7cbv
random_user_id() # wQ3DB4m9B5   81b6d51 
random_user_id() # Fzg7zE       i8pY5PNd11
random_user_id() # 7n9p0NZh     mkgjIY
random_user_id() # YWJ2cl       NW95K8Sm
random_user_id() # 743DqtlkjC   7IRZun