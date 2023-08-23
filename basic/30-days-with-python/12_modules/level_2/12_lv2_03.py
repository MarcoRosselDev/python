""" 3. Write a function generate_colors which can generate any number of hexa or rgb colors."""

""" output example:
    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
    generate_colors('hexa', 1) # ['#b334ef']
    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
    generate_colors('rgb', 1)  # ['rgb(33,79, 176)'] """

from random import randint

capital_letters = 'ABCDEF'
numbers = '0123456789'

def string_to_list(string):
    list_items = []
    for i in string:
        list_items.append(i)
    return list_items

capital_letters_list = string_to_list(capital_letters)
numbers_list = string_to_list(numbers)

def string_of_hexa_colors():
        hexa = '#'
        for each in range(0, 6):
            letter_or_number = randint(0, 1)
            if letter_or_number == 0:
                random_capital_letters = randint(0, len(capital_letters_list) - 1)
                hexa = hexa + capital_letters_list[random_capital_letters]
            elif letter_or_number == 1:
                random_number = randint(0, len(numbers_list) - 1)
                hexa = hexa + numbers_list[random_number]
            else:
                print('something is wrong')
        return hexa

def list_of_hexa_colors(times):
    list_hexa = []
    for j in range(0, times):
        list_hexa.append(string_of_hexa_colors())
    return list_hexa

def rgb_color_gen():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return str(f"rgb({r},{g},{b})")

def list_of_rgb_colors(times):
    list_rgb = []
    
    for each in range(0, times):
        list_rgb.append(rgb_color_gen())
    return list_rgb

def generate_colors(rgborhexa, times):
    if rgborhexa == 'hexa':
        print(list_of_hexa_colors(times))
    elif rgborhexa == 'rgb':
        print(list_of_rgb_colors(times))
    else:
        print('Enter a correct value please')

generate_colors('rgb', 6)
generate_colors('hexa', 4)
""" output
['rgb(48,145,35)', 'rgb(100,226,191)', 'rgb(16,51,167)', 'rgb(87,75,118)', 'rgb(93,237,220)', 'rgb(192,223,70)']
['#0EAACC', '#4A64E3', '#EC1DAF', '#677FC0'] """