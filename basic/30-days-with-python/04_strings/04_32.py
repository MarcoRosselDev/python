### 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

challenge = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
solution = ' # '.join(challenge)
print(solution)
### output --->    Django # Flask # Bottle # Pyramid # Falcon

### 33. Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.

challenge_33  = 'I am enjoying this challenge. \nI just wonder what is next.'
print(challenge_33)
""" I am enjoying this challenge. 
I just wonder what is next. """

""" 34. Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki """

challenge_34 = 'Name\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki'
print(challenge_34)
""" output :
Name		Age		Country		City
Asabeneh	250		Finland		Helsinki"""