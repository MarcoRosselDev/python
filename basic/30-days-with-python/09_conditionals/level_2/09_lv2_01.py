### 1. Write a code which gives grade to students according to theirs scores:

""" 
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F """

score = int(input('Enter your score please :'))

if score <= 49:
    print('you have an F')
elif score <= 59 and score >= 50:
    print('You have a D')
elif score <= 69 and score >= 60:
    print('You have a C')
elif score <= 89 and score >= 70:
    print('You have a B')
elif score <= 100 and score >= 90:
    print('You have an A')
else:
    print('Please enter a number between 0 - 100')