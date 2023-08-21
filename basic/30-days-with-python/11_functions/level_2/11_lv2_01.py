""" 1. Declare a function named evens_and_odds . 
It takes a positive integer as parameter and it counts 
number of evens and odds in the number. """

""" output example
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51. """

def evens_and_odds(num):
    sum_odds = 0
    sum_evens = 0
    for i in range(0, num + 1):
        if i%2 == 0:
            sum_evens += 1
        elif i%2 != 0:
            sum_odds += 1
        else:
            print(f'The value {i} return an Error')
    return print(f'The number of odds are {sum_odds}. \nThe number of evens are {sum_evens}.')

evens_and_odds(100)
# The number of odds are 50. 
# The number of evens are 51.
evens_and_odds(10)
# The number of odds are 5. 
# The number of evens are 6.