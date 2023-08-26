""" 5. Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}] """


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

solution = []
for sub_list in countries:
    new_dic = {}
    for tuples in sub_list:
        tuples = list(tuples)
        tuples[0] = tuples[0].upper()
        tuples[1] = tuples[1].upper()
        new_dic['country'] = tuples[0]
        new_dic['city'] = tuples[1]
    solution.append(new_dic)


print(solution)
""" 
[
{'country': 'FINLAND', 'city': 'HELSINKI'}, 
{'country': 'SWEDEN', 'city': 'STOCKHOLM'}, 
{'country': 'NORWAY', 'city': 'OSLO'}] """