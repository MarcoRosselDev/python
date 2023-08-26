list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

a = [box for box in list_of_lists for subcaja in box for box in subcaja ]

""" 4. Flatten the following list to a new list: 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], 
['SWEDEN', 'SWE', 'STOCKHOLM'], 
['NORWAY', 'NOR', 'OSLO']]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

for y in countries:
    final_list = []
    for pink in y:
        new_list = []
        pink = list(pink)
        for string in pink:
            string.upper()
            new_list.append(string)
        final_list.append(new_list)
    print(final_list)

""" output:
[['Finland', 'Helsinki']]
[['Sweden', 'Stockholm']]
[['Norway', 'Oslo']] """