""" 15. Declare a function named sum_of_even. 
It takes a number parameter and it adds all the 
even numbers in that - range. """

# even numbers = numeros pares

def sum_of_even(number):
    sum = 0
    for iterator in range(0, number + 1):
        if iterator%2 == 0:
            sum += iterator
        else:
            pass
    return print(sum)

sum_of_even(100) # 2550
sum_of_even(10) # 30