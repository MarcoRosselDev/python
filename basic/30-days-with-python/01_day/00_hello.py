# first coment
# this is my second coment

"""
there are a multy lineal coment using x3"
"""

print("string")

print(type("text")) # class str
print(type(4))      # class int
print(type(4.6))    # class float
print(type(4 + 1j)) # class complex
print(type(True))   # class bool

"""     In python we have the following additional operations:

3 % 2 = 1 => which means finding the remainder
3 // 2 = 1 => which means removing the remainder            """

# List
# Python list is anordered collection which allows to stare different data type items.

[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float

# Dictionary
# A python dictionary object is an unordered collection of data in a key value pair fromat.

{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}

# Tuple
# A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets

# Set
# A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

# In later sections, we will go in detail about each and every Python data type.

{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set