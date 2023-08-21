""" 10. Declare a function named capitalize_list_items. 
It takes a list as a parameter and it returns a capitalized list of items """

def capitalize_list_items(list):
    solution = []
    for item in list:
        solution.append(item.capitalize())
    return print(solution)


capitalize_list_items(['me gusta', 'python']) # ['Me gusta', 'Python']