# built in function append() 

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
# ['banana', 'orange', 'mango', 'lemon', 'apple']

fruits.append('lime')
print(fruits)
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# built in function insert
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)
# ['banana', 'orange', 'apple', 'mango', 'lemon', 'apple', 'lime']

fruits.insert(3, 'lime')
print(fruits)
# ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon', 'apple', 'lime']