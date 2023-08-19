### 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

# The sum of all evens is 2550. And the sum of all odds is 2500.
odds = 0
evens = 0

for num in range(0, 101):
    if num%2 == 0:
        evens = evens + num
        if(num == 100):
            print(f'The sum of all evens is {evens}')   #The sum of all evens is 2550
            print(f'The sum of all odds is {odds}')     # The sum of all odds is 2500
    else:
        odds = odds + num