# 3. Write a function which checks if all the items of the list are of the same data type.

def check_equal_types_in_list(list):
    list_check = set()
    for each in list:
        list_check.add(type(each))
    if len(list_check) > 1:
        print(f"The list {list} have more than one type of value")
    else:
        print(f"The list {list} have just one type of value")

check_equal_types_in_list([1, 3, 5, 6, 1])
# The list [1, 3, 5, 6, 1] have just one type of value
check_equal_types_in_list([1, 3, '5', 6, 1])
# The list [1, 3, '5', 6, 1] have more than one type of value