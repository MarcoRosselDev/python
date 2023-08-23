# 1. Writ a function which generates a six digit/character random_user_id.

""" example output:
print(random_user_id());
'1ee33d' """

from random import random, randint
from string import string

str_letters = string.ascii_letters
str_digits = string.digits

def random_user_id():
    print('break')