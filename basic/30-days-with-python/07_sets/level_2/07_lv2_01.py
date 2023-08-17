# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

### 1. Join A and B

print(A.isdisjoint(B)) # False
union = A.union(B)
print(union)                            # {19, 20, 22, 24, 25, 26, 27, 28}

### 2. Find A intersection B
intersection =  A.intersection(B)
print(intersection)                     # {19, 20, 22, 24, 25, 26}

### 3. Is A subset of B
is_ssubset = A.issubset(B)
print(is_ssubset)                       # True

### 4. Are A and B disjoint sets
is_disjoin = A.isdisjoint(B)
print(is_disjoin)                       # False

### 5. Join A with B and B with A
join_a_with_b = A.union(B)
print('join A with B : ', join_a_with_b)# join A with B :  {19, 20, 22, 24, 25, 26, 27, 28}

join_b_with_a = B.union(A)
print('join A with B : ', join_b_with_a)# join A with B :  {19, 20, 22, 24, 25, 26, 27, 28}

### 6. What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)             # {27, 28}

### 7. Delete the sets completely
del symmetric_difference
del join_a_with_b
del join_b_with_a
del is_disjoin                          # del ...