""" 3. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""

# Enter your age: 30
# You are 5 years older than me.

my_age = 30
your_age = int(input('Enter your age, please : '))

if my_age < your_age:
    missing_age = your_age - my_age
    print(f'You are {missing_age} years older than me')
elif my_age > your_age:
    missing_age = my_age - your_age
    print(f'You are {missing_age} years younger than me')
else:
    print('We have the same age!')