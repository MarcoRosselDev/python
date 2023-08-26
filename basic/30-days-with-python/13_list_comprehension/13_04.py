""" 4. Flatten the following list to a new list: 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

#a = [box for box in countries for num in box  for box  in num ]
f = []
for arr in countries:
    for tuple in arr:
        tuple = list(tuple)
        tuple.insert(1, tuple[0][:3])
        for item in range(len(tuple)):
            tuple[item] = tuple[item].upper()
        f.append(tuple)

print(f)

""" output:
[['FINLAND', 'FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']] """