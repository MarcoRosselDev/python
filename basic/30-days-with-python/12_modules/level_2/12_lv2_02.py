""" 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array. """
from random import randint

def list_of_rgb_colors(times):
    list_rgb = []
    def rgb_color_gen():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return str(f"rgb({r},{g},{b})")
    for each in range(0, times):
        list_rgb.append(rgb_color_gen())
    return list_rgb

print('first', list_of_rgb_colors(3))
print('/')
print('second one', list_of_rgb_colors(7))

""" output
first ['rgb(52,186,29)', 'rgb(79,170,40)', 'rgb(142,252,51)']
/
second one 
['rgb(182,140,20)', 'rgb(28,72,139)', 'rgb(212,182,214)', 
'rgb(215,90,49)', 'rgb(183,97,73)', 'rgb(110,183,227)', 'rgb(130,136,136)'] """