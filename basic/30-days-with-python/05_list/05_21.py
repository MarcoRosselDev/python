### 21. Remove the first IT company from the list
it_companies = ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
it_companies.remove('Oracle')
print(it_companies)
# ['Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

### 22. Remove the middle IT company or companies from the list
# print(len(it_companies)) # 6
del it_companies[2:4] # [0,1,2,3,4,5] <--- 2 = comienza incluyendolo, 4 = termina no incluyendolo
print('before del : ',it_companies)
# ['Microsoft', 'IBM', 'Apple', 'Amazon']

### 23. Remove the last IT company from the list
del it_companies[-1:]
print('delete last item : ',it_companies)
# delete last item :  ['Microsoft', 'IBM', 'Apple']

### 24. Remove all IT companies from the list
del it_companies[:]
print(it_companies) # []