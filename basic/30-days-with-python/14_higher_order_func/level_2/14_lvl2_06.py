""" 6. Use filter to filter out countries containing six letters and more in the country list. """
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def six_letters_and_more_out(item):
    if len(item) >= 6:
        return False
    else:
        return True

print(list(filter(six_letters_and_more_out, countries)))
# []