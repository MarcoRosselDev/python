""" 5. Use filter to filter out countries having exactly six characters. """

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_char_out(item):
    if len(item) == 6:
        return False
    else:
        return True

print(list(filter(six_char_out, countries)))
# ['Estonia', 'Finland', 'Denmark', 'Iceland']