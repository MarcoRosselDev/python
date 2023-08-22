""" 1. Write a function called is_prime, which checks if a number is prime. """

def is_prime(number):
    if type(number) == int:
        if number%2 == 0:
            print(f"'{number}' is not a prime number")
        else:
            print(f"'{number}' is a prime number")
    else:
        print(f"'{number}' is not a number")


"""     if type(number%2) == float or type(number%2) != int:
        print(f"This value : '{number}' is not a prime number")
    elif number/number == 1 and number/1 == number:
        print(f"This value: '{number}' is prime")
    else:
        print('?') """

is_prime(7)     # '7' is a prime number
is_prime(14)    # '14' is not a prime number
is_prime(17)    # '17' is a prime number
is_prime('6')   # '6' is not a number
is_prime(4)     # '4' is not a prime number
is_prime(89)     # '4' is not a prime number
is_prime(99)     # '4' is not a prime number