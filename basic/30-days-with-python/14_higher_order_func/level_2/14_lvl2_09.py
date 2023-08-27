""" 9. Declare a function called get_string_lists which takes a list 
as a parameter and then returns a list containing only string items. """

# modo convensional
def get_string_lists(lst):
    list_will_return = []
    for i in lst:
        to_string = str(i)
        list_will_return.append(to_string)
    return list_will_return

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = get_string_lists(numbers)
print(result)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']