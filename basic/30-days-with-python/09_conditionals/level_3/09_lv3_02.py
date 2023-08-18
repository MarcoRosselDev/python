# 2.    Check if the person dictionary has skills key, 
#       if so check if the person has 'Python' skill and print out the result.

person={
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

if 'skills' in person:
    if 'Python' in person['skills']:
        index = person['skills'].index('Python')
        print(person['skills'][index])                              # Python
    else:
        print('exist skills key but not Python value')
else:
    print("person dictionary doesn't have skills key value ")