""" 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number 
of IDs which are supposed to be generated. """

""" output example:
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr """

from random import randint

letters_min_list =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_may_list =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print(len(letters_min_list)) # 26
print(len(numbers_list))    # 10
print(len(letters_may_list)) # 26


def random_user_id(cuantity, lenght):
    random_leng_id = randint(0, lenght) # largo aleatoria entre 6 y 10 digitos
    id = '' # string donde agregar los valores en cada iteracion
    for i in range(0, cuantity):
        for iteration in range(0, random_leng_id):
            random_type_list = randint(0, 2)
            if random_type_list == 0:   # si es 0 iteramos aleatoriamente por la lista de letras minusculas
                random_letters_list_index = randint(0, len(letters_min_list) - 1 )
                id = id + letters_min_list[random_letters_list_index]
            elif random_type_list == 1:     # si es 1 iteramos aleatoriamente por la lista de numeros
                random_numbers_list_index = randint(0, len(numbers_list) - 1)
                id = id + numbers_list[random_numbers_list_index]
            elif random_type_list == 2:     # si es 2 iteramos aleatoriamente por la lista de letras mayusculas
                random_letters_list_mayusc_index = randint(0, len(letters_may_list) - 1 )
                id = id + letters_may_list[random_letters_list_mayusc_index]
            else:
                id = id + ''
    print(id)

random_user_id(5, 5) # is not working