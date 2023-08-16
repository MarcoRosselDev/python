### 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
""" 
a-Sort the list and find the min and max age
b-Add the min age and the max age again to the list
c-Find the median age (one middle item or two middle items divided by two)
d-Find the average age (sum of all items divided by their number )
e-Find the range of the ages (max minus min)
f-Compare the value of (min - average) and (max - average), use abs() method
"""
# a-------------------------------------------------------------
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print('The min age is : ', min_age)
# The min age is :  19
print('The max age is : ', max_age)
# The max age is :  26

# b--------------------------------------------------------------
add_end = min_age + max_age
print(add_end)
print('ages before add : ', ages)