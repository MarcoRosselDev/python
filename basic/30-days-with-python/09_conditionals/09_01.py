### 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

""" 
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive. """

age_user = int(input('Enter your age please : '))

if age_user > 18:
    print('You are old enough to drive.')
else:
    missing_age = 18 - age_user
    print(f'you need {missing_age} more years to learn to drive')