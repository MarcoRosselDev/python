from random import randint

letters_min_list =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_may_list =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def random_one(length):
    id = ''                                                                             # string donde agregar los valores en cada iteracion
    for iteration in range(0, length):
        random_type_list = randint(0, 2)
        if random_type_list == 0:                                                       # si es 0 iteramos aleatoriamente por la lista de letras minusculas
            random_letters_list_index = randint(0, len(letters_min_list) - 1 )
            id = id + letters_min_list[random_letters_list_index]
        elif random_type_list == 1:                                                     # si es 1 iteramos aleatoriamente por la lista de numeros
            random_numbers_list_index = randint(0, len(numbers_list) - 1)
            id = id + numbers_list[random_numbers_list_index]
        elif random_type_list == 2:                                                     # si es 2 iteramos aleatoriamente por la lista de letras mayusculas
            random_letters_list_mayusc_index = randint(0, len(letters_may_list) - 1 )
            id = id + letters_may_list[random_letters_list_mayusc_index]
        else:
            id = id + ''
    return id

def random_user_id(repetitions):
    for any in range(0, repetitions):
        random_one()
