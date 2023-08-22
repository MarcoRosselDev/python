# 2. Write a functions which checks if all items are unique in the list.

def check_unique_values(list):
    copy_list = list.copy()
    copy_list = set(copy_list)
    if len(list) == len(copy_list):
        print('check list successfull, each item are unique')
    else:
        print('check list filed, some value is repited')


check_unique_values([2,4,6,1])   # check list successfull, each item are unique
check_unique_values([2,4,6,1,1]) # check list filed, some value is repited