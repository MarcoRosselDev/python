""" 1. Use map to create a new list by changing each country to uppercase in the countries list """

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def to_upper(item):
    return item.upper()

print(list(map(to_upper, countries)))
# ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']