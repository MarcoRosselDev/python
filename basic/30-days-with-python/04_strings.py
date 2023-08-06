# Strings

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
a, b, c, d = 'Thirty', 'Days', 'of', 'Python'
exercise_01 = '{} {} {} {}'.format(a, b, c, d)
print(exercise_01) # Thirty Days of Python

# 2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
e, f, g = 'Coding', 'For', 'All'
exercise_02 = '{} {} {}'.format(e, f, g)
print(exercise_02) # Coding For All

# 3.Declare a variable named company and assign it to an initial value "Coding For All".
company = exercise_02

# 4.Print the variable company using print().
print(company)

# 5.Print the length of the company string using len() method and print().
print(len(company)) # 14

# 6.Change all the characters to uppercase letters using upper() method.
print(company.upper()) # CODING FOR ALL