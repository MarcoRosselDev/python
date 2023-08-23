""" 3 Write a function named rgb_color_gen. 
It will generate rgb colors (3 values ranging from 0 to 255 each). """

""" 
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form """
from random import randint

def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return print(f"rgb({r},{g},{b})")

rgb_color_gen()
rgb_color_gen()
rgb_color_gen()
rgb_color_gen()
rgb_color_gen()
rgb_color_gen()

""" output:
rgb(139,44,0)
rgb(120,243,218)
rgb(30,176,202)
rgb(220,124,112)
rgb(140,194,135)
rgb(64,106,44) """