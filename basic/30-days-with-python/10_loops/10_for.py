# for in list
""" numbers = [1, 2, 3, 4, 5, 'Hi', False]

for a in numbers:
    print(a) """

# for in string

""" my_string = 'marco'

for a in my_string:
    print(a) """

# for in dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for a in person:
    print(a)
""" 
first_name
last_name
age
country
is_marred
skills
address """

for a, b in person.items():
    print(a, b) # this way we get both keys and values printed out

""" 
first_name Asabeneh
last_name Yetayeh
age 250
country Finland
is_marred True
skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
address {'street': 'Space street', 'zipcode': '02210'} """
# siempre el primer valor sera la key en for dictiionary
# y el segundo valor si es que te intereza sera el value
# para una mejor sintaxis no usar a, b, si no key, value.
