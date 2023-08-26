""" 4. Use filter to filter out countries containing 'land'. """

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def land_out(item):
    if 'land' in item:
        return False
    else:
        return True

print(list(filter(land_out, countries)))
# ['Estonia', 'Sweden', 'Denmark', 'Norway']