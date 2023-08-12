language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

## reversing a String
#  We can easily reverse strings in python.

greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

## Skipping Characters While Slicing
#  It is possible to skip characters while slicing by passing step argument to slice method.
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto