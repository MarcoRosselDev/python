it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

### 14. Join the it_companies with a string '#;  '
list_join = "#; ".join(it_companies)
print(list_join)
# FACEBOOK#; Google#; Microsoft#; Apple#; Github#; IBM#; Oracle#; Mercado Libre#; Amazon

### 15. Check if a certain company exists in the it_companies list.
does_exist = 'IBM' in it_companies
print('IBM is in IT list? : ',does_exist)
# IBM is in IT list? :  True

### 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
# ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle']
# ahora esta ordenada en orden alfavetico

### 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']
# ahora esta en orden descendente

### 18. Slice out the first 3 companies from the list
new_list = it_companies[3:]
print('new list : ', new_list)
# new list :  ['Google', 'Facebook', 'Apple', 'Amazon']

