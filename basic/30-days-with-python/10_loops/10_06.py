### 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

print('this is whit for loop')
for item in my_list:
    print(item)


print('this is whit while loop')
count = 0
while count < len(my_list):
    print(my_list[count])
    count =  count + 1

""" output
this is whit for loop
Python
Numpy
Pandas
Django
Flask
this is whit while loop
Python
Numpy
Pandas
Django
Flask """