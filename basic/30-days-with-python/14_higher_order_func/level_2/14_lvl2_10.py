""" 10. Use reduce to sum all the numbers in the numbers list. """
# para resolver el error:
# NameError: name 'reduce' is not defined ----> importamos reduce from functools
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(reduce(lambda a, b: a + b, numbers))