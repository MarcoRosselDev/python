# Day 3 ---> Boolean

# print(1 is 1)               # true
# print(1 is not 2)           # true
# print('A' in "Asabeneh")    # true

""" Logical Operators
Unlike other programming languages python uses keywords and, or and not for logical operators. Logical operators are used to combine conditional statements: """

# and -- return true if both statements are true
print('operador and : 1 < 5 and 2 > 1 = ', 1 < 5 and 2 > 1) # true

# or -- return true if one of the statements is true
print('operador or : 1 < 5 or 1  > 10 = ', 1 < 5 or 1 > 10) # true

# not -- reverse the result, return false if the result is ture
print('operador not :  not(2 < 5) = ', not(2 < 5)) # false


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

# 1. Declare your age as integer variable
my_age = 30
# 2. Declare your height as a float variable
my_height = 1.71 # meters
# 3. Declare a variable that store a complex number
complex_number = 1j
print("compelx number 1j =", complex_number)
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = 4
height = 6
area = base * height * 0.5
print("area triangle = ", area)
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
lado = 4
triangle_perimeter = lado + lado + base
print('perimetro de triangulo = ', triangle_perimeter)
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length_rectangle = 8
width_rectangle = 4
area_rectangel = length_rectangle * width_rectangle
print("area rectangle = ", area_rectangel)
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2