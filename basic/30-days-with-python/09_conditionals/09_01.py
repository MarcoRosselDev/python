### 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age_user = int(input('Enter your age please : '))

if age_user > 18:
    print('You are old enough to drive.')
else:
    print('Wait for the missing amount of years')