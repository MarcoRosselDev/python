### 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.

# The sum of all numbers is 5050.
suma = 0
for num in range(0, 101):
    suma = suma + num
    if(num == 100):
        print(f'The sum of all numbers is {suma}') # The sum of all numbers is 5050