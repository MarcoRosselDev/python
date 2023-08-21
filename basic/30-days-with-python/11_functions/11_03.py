### 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def sum_all_nums(*nums):
    suma = 0
    for num in nums:
        if type(num) == int or type(num) == float:
            suma += num
        else:
            print(f'El valor {num} no es un numero int')
    return suma

print(sum_all_nums(1,2,3,4)) # 10
print(sum_all_nums(1,2,3,"4")) # El valor 4 no es un numero int
print(sum_all_nums(1,2,3,"Hi")) # El valor Hi no es un numero int 