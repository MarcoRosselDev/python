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