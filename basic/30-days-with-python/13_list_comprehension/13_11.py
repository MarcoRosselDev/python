list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

a = [box for box in list_of_lists for subcaja in box for box in subcaja ]

""" 4. Flatten the following list to a new list: 
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], 
['SWEDEN', 'SWE', 'STOCKHOLM'], 
['NORWAY', 'NOR', 'OSLO']]"""

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

b = [box for box in countries for i in box]


for box in countries:
    f = []
    for sub_box in box:
        f = []
        sub_box = list(sub_box)
        sub_box.insert(1, sub_box[0][:3])
        sub_list = []
        for i in sub_box:
            i = i.upper()
            sub_list.append(i)
    print(f)
