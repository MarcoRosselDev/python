### 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

""" 
If a fruit doesn't exist in the list add the fruit to the list and print 
the modified list. If the fruit exists print('That fruit already exist in the 
list')
"""

fruit = input('Enter any fruit please : ')

if (fruit in fruits) == True:
    print('That fruit is already exist in the list')
elif (fruit in fruits) == False:
    fruits.append(fruit)
    print(fruits)
else:
    print("You don't enter a fruit correctly")