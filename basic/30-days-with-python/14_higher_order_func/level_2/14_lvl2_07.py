""" 7. Use filter to filter out countries starting with an 'E' """

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'ecuador', 'chile']

def start_with_e_out(item):
    if item[0] == 'E' or item[0] == 'e':
        return False
    else:
        return True

print(list(filter(start_with_e_out, countries)))
# ['Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'chile']