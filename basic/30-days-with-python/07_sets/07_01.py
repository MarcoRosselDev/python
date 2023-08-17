# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### 1. Find the length of the set it_companies--------------------------
print(len(it_companies))
# 7

### 2. Add 'Twitter' to it_companies------------------------------------
it_companies.add('Twitter')
print(it_companies)
# {'Facebook', 'Amazon', 'Google', 'Microsoft', 'Oracle', 'Twitter', 'Apple', 'IBM'}

### 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Samsung Electronics','Alphabet','China Mobile'])
print(it_companies)
# {'Twitter', 'Alphabet', 'Microsoft', 'Samsung Electronics', 'IBM', 'China Mobile', 'Google', 'Oracle', 'Facebook', 'Apple', 'Amazon'}

### 4. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print(it_companies)
# {'Amazon', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Alphabet', 'Twitter', 'Samsung Electronics', 'Apple', 'China Mobile'}

### 5. What is the difference between remove and discard
    # remove(elem): Remove element elem from the set. Raises KeyError if elem is not contained in the set.

    # discard(elem): Remove element elem from the set if it is present.