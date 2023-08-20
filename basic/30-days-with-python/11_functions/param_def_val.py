""" Function with Default Parameters
Sometimes we pass default values to parameters, when we invoke the function. 
If we do not pass arguments when calling the function, their default values will be used """

def greetings (name = 'Peter'): # si no le aplicamos un argumento se aplica Peter por defecto
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())              # Peter, welcome to Python for Everyone!
print(greetings('Asabeneh'))    # Asabeneh, welcome to Python for Everyone!

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())                 # Asabeneh Yetayeh
print(generate_full_name('David','Smith'))  # David Smith

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon