""" 15. Declare a get_last_ten_countries function 
that returns the last ten countries in the countries list. """
from countries import countries

def get_last_ten(listt):
    last_10_list = []
    for i in range(0, len(listt)):
        if i >= (len(listt) - 10):
            last_10_list.append(listt[i])
        else:
            pass
    return last_10_list


solution = get_last_ten(countries)
print(solution)
""" output:
['United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 
'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'] """