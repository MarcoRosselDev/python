### 1. Create an empty tuple
empty_tuple = tuple()
print(empty_tuple) # ()

### 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

my_brothers = ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco')
my_sisters = ('Eva', 'Delia')
# ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco', 'Eva', 'Delia')

### 3. Join brothers and sisters tuples and assign it to siblings
brothers = my_brothers + my_sisters
print(brothers)

### 4. How many siblings do you have?
num_brothers = len(brothers)
print(num_brothers) # 6

### 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
brothers = list(brothers)
print(brothers)
brothers.append('Camila')
brothers.append('Constantine')
brothers = tuple(brothers)
print(brothers)
# ('Eduardo', 'Juan', 'Eduardo Jr', 'Marco', 'Eva', 'Delia', 'Camila', 'Constantine')