""" 11.  Use reduce to concatenate all the countries and to produce this sentence: 
    Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries"""
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def concat_strings(*items):
    string_return = ''
    for each in items:
        if each == items[0]:
            string_return += f'{each}'
        elif each == each[-1]:
            string_return += f' and {each} are north European countries'
        else:
            string_return += f', {each}'
    return string_return

outside = concat_strings(countries)
print(outside)


result = str(reduce(concat_strings, countries))
print(result) # Estonia, Finland, Sweden, Denmark, Norway, Iceland
print(type(result)) # str