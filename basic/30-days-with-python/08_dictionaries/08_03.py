### 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = dict()
student['first_name'] = 'Marco'
student['last_name'] = 'Rossel'
student['gender'] = False
student['age'] = 30
student['marital'] = False
student['skills'] = ['JavaScript', 'React', 'Python', 'NodeJS']
student['country'] = 'Chilean'
student['city'] = 'Concepcion'
student['address'] = {
    'n_house' : 522,
    'n_street' : 'nueva los copihues'
}

### 4. Get the length of the student dictionary
print(len(student))         # 9

### 5. Get the value of skills and check the data type, it should be a list
