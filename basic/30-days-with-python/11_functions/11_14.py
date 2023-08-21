""" 14. Declare a function named sum_of_odds. 
It takes a number parameter and it adds all the odd numbers in that range. """

def sum_of_odds(value):
    sum = 0
    for num in range(0, value + 1):
        if num%2 != 0:
            sum += num
        else:
            pass
    return print(sum)

sum_of_odds(100) # 2500
sum_of_odds(11)