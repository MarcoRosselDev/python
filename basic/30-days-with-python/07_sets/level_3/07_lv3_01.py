# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print('len of age with list : ', len(age))      # len of age with list :  8

age = set(age)
print('len of age with set : ', len(age))       # len of age with set :  5
# cuando pasamos una lista a set, no pueden tener elementos repetidos, por eso el len es diferente.