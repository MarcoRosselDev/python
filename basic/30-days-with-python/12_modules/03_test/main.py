# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
from random import randint
from random_id import random_one
# random_user_id take 2 arguments, 1 = lenght_id, 2 = times

def shuffle_list(lista):
    id_dictionary = {}
    lista_random = []
    key_list = []
    for i in lista:
        id_dictionary[random_one(9)] = i
    for j in id_dictionary.keys():
        key_list.append(j)
    key_list.sort()
    for k in key_list:
        lista_random.append(id_dictionary[k])
    print(lista_random)

shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])
shuffle_list([1, False, 'Hi', True, 2])

""" output
[True, False, 1, 'Hi', 2]
[True, 'Hi', False, 2, 1]
[False, 2, 'Hi', True, 1]
[True, 2, False, 1, 'Hi']
['Hi', False, 1, 2, True]
['Hi', True, 1, 2, False]
[1, False, 'Hi', True, 2] """