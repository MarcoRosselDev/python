""" 12. Declare a function called categorize_countries that returns 
a list of countries with some common pattern 
(you can find the countries list in this repository as 
countries.js(eg 'land', 'ia', 'island', 'stan')). """
# https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py

from countries import countries

#print(countries[0])

def comon_pattern(*items):
    for i in items:
        # we can use any string methods tho match results
        # count(), endwith(), find(), rfind(),
        if i.find('land') != -1:
            return True
        else:
            return False

solution = list(filter(comon_pattern, countries))
print(solution)
print(len(solution), 'length solution') # 11 length solution
print(len(countries), 'length countries') # 193 length countries 

""" output:
['Finland', 'Iceland', 'Ireland', 'Marshall Islands', 
'Netherlands', 'New Zealand', 'Poland', 'Solomon Islands', 
'Swaziland', 'Switzerland', 'Thailand']
"""