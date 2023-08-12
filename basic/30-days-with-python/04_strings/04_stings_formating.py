""" % Operator 

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision 
"""

nombre = 'Marco'
edad = 30
random_float_number = 4.14435312343

formating = 'I, my name is %s, I have %d years old, and my luky number is %.3f, bay' %(nombre, edad, random_float_number)
print(formating)
# I, my name is Marco, I have 30 years old, and my luky number is 4.144, bay

""" this is a new form of formating strings with variables """

new_form_formating = 'Hola mi nombre es {}, tengo {} de edad y mi numero de la suerte es el {:.3f}'.format(nombre, edad, random_float_number)
print(new_form_formating)
## Hola mi nombre es Marco, tengo 30 de edad y mi numero de la suerte es el 4.144

""" tercera forma de agregar variables en los strings """

print(f'Tercera forma, mi nombre es {nombre}, tengo {edad} agnios, y mi numero de la suerte es {random_float_number:.2f}')
## Tercera forma, mi nombre es Marco, tengo 30 agnios, y mi numero de la suerte es 4.14