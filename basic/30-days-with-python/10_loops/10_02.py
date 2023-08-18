### 2. Iterate 10 to 0 using for loop, do the same using while loop.

my_list = list(range(0, 11))
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.reverse()
print(my_list)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print('this is using for')
for number in my_list:
    print(number)

print('this is using while')
loop = 11
while loop > 0:
    loop = loop - 1
    print(loop)

""" output
this is using for
10
9
8
7
6
5
4
3
2
1
0
this is using while
10
9
8
7
6
5
4
3
2
1
0
"""