### Level 3
""" 
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary """

number_integer_example = 13
number_float_example = 3.14
number_complex_example = 5j

sting_example = 'Hello!'
boolean_example = True
list_example = [True, 'sting', ['another list', 'inside of another list', True, 4j], 13, (2, 3, 'text')]

diccionary_example = {
    'name': 'marco',
    'last_name': 'rossel',
    'age': 30,
    'country': 'chileno',
    'data': ['text', 'random', 20, False],
    'dicctionary': {
        'another_list': True,
        'subname': 'moko'
    },
    'casado': False
}

tupla_example = (2, 43, 1, 'text', True)

print(type(number_integer_example)) # <class 'int'>
print(type(number_float_example)) # <class 'float'>
print(type(number_complex_example)) # <class 'complex'>
print(type(sting_example)) # <class 'str'>
print(type(boolean_example)) # <class 'bool'>
print(type(list_example)) # <class 'list'>
print(type(diccionary_example)) # <class 'dict'>
print(type(tupla_example)) # <class 'tuple'>