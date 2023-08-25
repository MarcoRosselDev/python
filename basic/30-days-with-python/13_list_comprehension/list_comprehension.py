# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

positive_numbers = [i for i in numbers if i > 0]
print(positive_numbers)
positive_even_numbers = [i for i in numbers if i%2 == 0 and i>0]
print(positive_even_numbers)