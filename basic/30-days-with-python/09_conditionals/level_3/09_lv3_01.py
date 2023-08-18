### 1. Here we have a person dictionary. Feel free to modify it!

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

# a. * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if ('skills' in person) == True:
    lenth_list_skills = len(person['skills'])
    print(person['skills'][int(lenth_list_skills/2)])   # Node