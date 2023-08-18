""" 4. If the person is married and if he lives in Finland, 
print the information in the following format:"""

#    Asabeneh Yetayeh lives in Finland. He is married.

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['is_marred'] == True and person['country'] == 'Finland':
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married')
    # Asabeneh Yetayeh lives in Finland. He is married