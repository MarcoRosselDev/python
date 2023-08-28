""" 14. Declare a get_first_ten_countries 
function - it returns a list of first ten countries 
from the countries.js list in the data folder. """
from countries import countries

def get_first_ten_countries(listt):
    list_10_countries = []
    for i in range(0, len(listt)):
        if i < 10:
            list_10_countries.append(listt[i])
    return list_10_countries

solution = get_first_ten_countries(countries)
print(solution)

""" output:
['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 
'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria'] """