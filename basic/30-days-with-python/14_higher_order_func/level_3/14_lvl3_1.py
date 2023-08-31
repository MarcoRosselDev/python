""" 1. Use the countries_data.py 
(https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 
file and follow the tasks below: """
# Sort countries by name, by capital, by population

from countries_data import dict_countries
print(dict_countries[0])

for i in dict_countries:
    print(i['capital'])