""" 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors 
in an array (six hexadecimal numbers written after #. 
Hexadecimal numeral system is made out of 16 symbols, 
0-9 and first 6 letters of the alphabet, a-f. 
Check the task 6 for output examples).
"""
# example : #b71a9f
from random import randint

capital_letters = 'ABCDEF'
numbers = '0123456789'

def string_to_list(string):
    list_items = []
    for i in string:
        list_items.append(i)
    return list_items

capital_letters_list = string_to_list(capital_letters)
numbers_list = string_to_list(numbers)

def list_of_hexa_colors():
    hexa = '#'
    for each in range(0, 6):
        letter_or_number = randint(0, 1)
        if letter_or_number == 0:
            random_capital_letters = randint(0, len(capital_letters_list) - 1)
            hexa = hexa + capital_letters_list[random_capital_letters]
        elif letter_or_number == 1:
            random_number = randint(0, len(numbers_list) - 1)
            hexa = hexa + numbers_list[random_number]
        else:
            print('something is wrong')
    print(hexa)

#test
list_of_hexa_colors()
list_of_hexa_colors()
list_of_hexa_colors()
list_of_hexa_colors()
list_of_hexa_colors()

""" output
#FBFC71
#50B5CB
#4B371C
#AA26CD
#C14B6B """