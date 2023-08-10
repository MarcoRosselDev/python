first_name = 'Marco'
last_name = 'Rossel'
full_name = first_name + ' ' + last_name
country = 'Chileno'
city = 'Concepcion'
age = 30
year = 2023
is_married = False
is_true = True
is_light_on = False
a, b, c, d = 1, 4, 6, 2 

# 1. Check the data type of all your variables using type() built-in function

print(type(first_name)) # <class 'str'>
print(type(last_name)) # <class 'str'>
print(type(full_name)) # <class 'str'>
print(type(country)) # <class 'str'>
print(type(city)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(year)) # <class 'int'>
print(type(is_married)) # <class 'bool'>
print(type(is_true)) # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>
print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'int'>

# 2. Using the _len()_ built-in function, find the length of your first name--

print("mi first name length : ",len(first_name)) 
# mi first name length :  5

### 3. Compare the length of your first name and your last name----------------
print("mi first name length : ",len(first_name), "mi last name length : ", len(last_name))
## mi first name length :  5 mi last name length :  6

### 4. Declare 5 as num_one and 4 as num_two-----------------------------------
num_one = 5
num_two = 4
# a. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print('add : ', total) # 9

# b. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
print('subtract : ', diff) # 1

# c. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two
print('multiply : ', product) # 20

# d. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print('division : ', division) # 1.25

# e. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print('reminder : ', remainder) # 4

# f. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print('exponent : ', exp) # 625

# g. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('floor_division : ', floor_division) # 1

""" output

add :  9
subtract :  1
multiply :  20
division :  1.25
reminder :  4
exponent :  625
floor_division :  1
"""

### 5. The radius of a circle is 30 meters.

# a. Calculate the area of a circle and assign the value to a variable name of area_of_circle

radius_circle = 30 # meters
pi = 3.14
area_of_circle = (radius_circle ** 2) * pi
print('area del circulo : ', area_of_circle) # area del circulo :  2826.0

# b. Calculate the circumference of a  circle and assign the value to a variable name of circum_of_circle

circumference_circle = radius_circle * 2 * pi
print('perimetro circulo : ', circumference_circle) # perimetro circulo :  188.4

# c. Take radius as user input and calculate the area.

radius_circle_input = int(input('input a radius please : '))
area_of_circle_input = (radius_circle_input ** 2) * pi
print('area circle from input : ', area_of_circle_input)