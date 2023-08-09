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

# 2. Using the _len()_ built-in function, find the length of your first name

print("mi first name length : ",len(first_name)) 
# mi first name length :  5

### 3. Compare the length of your first name and your last name
print("mi first name length : ",len(first_name), "mi last name length : ", len(last_name))
## mi first name length :  5 mi last name length :  6

