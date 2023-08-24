# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
from random import randint
from random_id import random_one
# random_user_id take 2 arguments, 1 = lenght_id, 2 = times

def shuffle_list(lista):
    id_dictionary = {}
    lista_random = []
    for i in lista:
        id_dictionary[random_one(9)] = i
    
    
    for j in id_dictionary:
        lista_random.append(id_dictionary[j])
    print(lista_random)

shuffle_list([1, False, 'Hi', True, 2])