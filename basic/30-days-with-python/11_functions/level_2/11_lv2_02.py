""" 2. Call your function factorial, 
it takes a whole number as a parameter and 
it return a factorial of the number """

def factorial(value):
    numbers = []
    if value%2 == 0:
        numbers.append(value)
        n = value/2
        if n%2 == 0:
            numbers.append(n)
            i = value/2
            if i%2 == 0:
                numbers.append(i)
            else:
                'no more numbers'
        else:
                'no more numbers'
    else:
                'no div for 2'
    return print(numbers)

factorial(10)