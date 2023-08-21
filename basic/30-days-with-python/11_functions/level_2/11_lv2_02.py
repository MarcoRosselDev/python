""" 2. Call your function factorial, 
it takes a whole number as a parameter and 
it return a factorial of the number """

def factorial(number):
    sum = 1
    for i in range(1, number + 1):
        sum = sum*i
    return print(sum)

factorial(5) # 120
factorial(6) # 720