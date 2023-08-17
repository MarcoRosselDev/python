### 3. Create a student dictionary and add first_name, last_name, gender, 
### age, marital status, skills, country, city and address as keys for the dictionary------------

student = dict()
student['first_name'] = 'Marco'
student['last_name'] = 'Rossel'
student['gender'] = 'Male'
student['age'] = 30
student['marital'] = False
student['skills'] = ['JavaScript', 'React', 'Python', 'NodeJS']
student['country'] = 'Chilean'
student['city'] = 'Concepcion'
student['address'] = {
    'n_house' : 522,
    'n_street' : 'nueva los copihues'
}

### 4. Get the length of the student dictionary----------------------------------------------------
print(len(student))         # 9

### 5. Get the value of skills and check the data type, it should be a list------------------------

print('value of skills : ', student['skills'])
# value of skills :  ['JavaScript', 'React', 'Python', 'NodeJS']

print('data type of skills : ', type(student['skills']))
# data type of skills :  <class 'list'>

### 6. Modify the skills values by adding one or two skills----------------------------------------
student['skills'] = student['skills'] + ['Git', 'TypeScript']
print('students skills after edition : ', student['skills'])
# students skills after edition :  ['JavaScript', 'React', 'Python', 'NodeJS', 'Git', 
# 'TypeScript']

### 7. Get the dictionary keys as a list-----------------------------------------------------------
print(student.keys())
# dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital', 'skills', 'country', 
# 'city', 'address'])

### 8. Get the dictionary values as a list---------------------------------------------------------
print(student.values())
# dict_values(['Marco', 'Rossel', 'Male', 30, False, ['JavaScript', 'React', 'Python', 
# 'NodeJS', 'Git', 'TypeScript'], 'Chilean', 'Concepcion', 
# {'n_house': 522, 'n_street': 'nueva los copihues'}])

### 9. Change the dictionary to a list of tuples using items() method------------------------------
change_tuples = student.items()
print(change_tuples)
# dict_items([('first_name', 'Marco'), ('last_name', 'Rossel'), ('gender', 'Male'), 
# ('age', 30), ('marital', False), ('skills', ['JavaScript', 'React', 'Python', 'NodeJS', 'Git', 
# 'TypeScript']), ('country', 'Chilean'), ('city', 'Concepcion'), ('address', 
# {'n_house': 522, 'n_street': 'nueva los copihues'})])

### 10. Delete one of the items in the dictionary--------------------------------------------------
del student['address']
del student['skills']

print(student)
# {'first_name': 'Marco', 'last_name': 'Rossel', 'gender': 'Male', 'age': 30, 'marital': False, 
# 'country': 'Chilean', 'city': 'Concepcion'}

### 11. Delete one of the dictionaries
del student
print(student)  # None