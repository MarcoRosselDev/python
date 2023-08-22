""" 3. Call your function is_empty, 
it takes a parameter and it checks if it is empty or not"""

def is_empty(param):
    if type(param) == int or type(param) == float:
        if param == 0:
            print('The 0 is nos empty, is just an ausent value')
        else:
            print(f'{param} is not empty')
    elif type(param) == dict or type(param) == tuple or type(param) == list or type(param) == set or type(param) == str:
        if len(param) == 0:
            print(f"This value [{param}] is empty")
        else:
            print(f"This value [{param}] is not empty, it has {len(param)} of lenght")

is_empty('Hi')
is_empty(6)
is_empty('')
is_empty(' ')
is_empty([])

""" output:
This value [Hi] is not empty, it has 2 of lenght
6 is not empty
This value [] is empty
This value [ ] is not empty, it has 1 of lenght
This value [[]] is empty """