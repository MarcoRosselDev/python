""" 3. Use map to change each name to uppercase in the names list """

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

def to_upper(item):
    return item.upper()

print(list(map(to_upper, names)))
# ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']