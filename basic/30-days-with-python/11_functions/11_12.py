""" 12. Declare a function named remove_item. 
It takes a list and an item parameters. 
It returns a list with the item removed from it. """

""" exampleÑ
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
;
print(remove_item(numbers, 3))  # [2, 7, 9] """

def remove_item(list, item):
    list.remove(item)
    return print(list)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] # ['Potato', 'Tomato', 'Milk']
remove_item(food_staff, 'Mango')
numbers = [2, 3, 7, 9]
remove_item(numbers, 3) # [2, 7, 9]