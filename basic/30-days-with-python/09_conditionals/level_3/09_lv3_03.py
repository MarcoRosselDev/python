""" 3.  * If a person skills has only JavaScript and React, print
('He is a front end developer'), if the person skills has Node, 
Python, MongoDB, print('He is a backend developer'), if the person 
skills has React, Node and MongoDB, Print('He is a fullstack 
developer'), else print('unknown title') - for more accurate results 
more conditions can be nested!
"""
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

if 'skills' in person:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a backend developer')
    elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print("person dictionary doesn't have skills key value ")