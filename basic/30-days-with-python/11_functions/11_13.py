""" 13. Declare a function named sum_of_numbers. 
It takes a number parameter and it adds all the numbers in that range. """

""" example:
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050 """

def sum_of_numbers(num):
    sum = 0
    for i in range(0, num + 1):
        sum += i
    return print(sum)

sum_of_numbers(5) # 15
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050