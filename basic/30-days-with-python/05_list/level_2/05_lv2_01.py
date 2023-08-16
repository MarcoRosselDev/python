### 1. The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a-------------------------------------------------------------
# a-Sort the list and find the min and max age
ages.sort()
print('ages before sort function', ages)
min_age = ages[0]
max_age = ages[-1]
print('The min age is : ', min_age)
# The min age is :  19
print('The max age is : ', max_age)
# The max age is :  26

# b--------------------------------------------------------------
# b-Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.insert(-1, max_age)
print('ages before add : ', ages)

# c--------------------------------------------------------------
# c-Find the median age (one middle item or two middle items divided by two)
""" 
numbers = [2, 3, 3, 5, 7 , 10]
sum = sum(numbers) # 30
print('la suma de numbers is : ', sum)
media = sum / len(numbers)
print('la mediana de numbers es : ', media) # 5.0
"""
ages_lenght = len(ages)
print('ages lenght ', ages_lenght)
# ages lenght  12
middle_age =int((ages[5] + ages[6]) / 2)
print('la edad media es ', middle_age)
# la edad media es  24
# d--------------------------------------------------------------
# d-Find the average age (sum of all items divided by their number )
sum_ages = sum(ages)
median_age = sum_ages / len(ages)
print('la mediana de ages es: ', median_age)
# la mediana de ages es:  22.75

# e--------------------------------------------------------------
# e-Find the range of the ages (max minus min)
# f--------------------------------------------------------------
# f-Compare the value of (min - average) and (max - average), use abs() method