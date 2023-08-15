### 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_type = ['marco', 30, 1.72, 'soltero', 'nueva los copihues, 522']

### 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

### 7. Print the list using print()
print(it_companies)
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

### 8. Print the number of companies in the list
print(len(it_companies)) # 7

### 9. Print the first, middle and last company
print(it_companies[0], it_companies[3], it_companies[-1])
# Facebook Apple Amazon

### 10. Print the list after modifying one of the companies
it_companies[-1] = 'Mercado Libre'
print(it_companies)
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Mercado Libre']

### 11. Add an IT company to it_companies
it_companies.append('Amazon')

### 12. Insert an IT company in the middle of the companies list
print('the length of IT company list : ', len(it_companies))
# the length of IT company list :  8
# sabiendo esto podemos agregar la IT company en la posicion 3 que es igual a la 4
it_companies.insert(4, 'Github')
print('it companies add in the midle : ', it_companies)
# it companies add in the midle :  
# ['Facebook', 'Google', 'Microsoft', 'Apple', 'Github', 'IBM', 'Oracle', 'Mercado Libre', 'Amazon']

### 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print('upper = change to uppercase : ', it_companies)
# swapcase = change to uppercase :  
# ['FACEBOOK', 'Google', 'Microsoft', 'Apple', 'Github', 'IBM', 'Oracle', 'Mercado Libre', 'Amazon']