""" 2. Use map to create a new list by changing each number to its square in the numbers list """

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_nums(item):
    return item**2

print(list(map(square_nums, numbers)))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]