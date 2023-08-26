""" 7. Write a lambda function which can solve a slope or y-intercept of linear functions. """

m = lambda x1, y1, x2, y2: (x2 - x1)/(y2 - y1)

print(m(0, 0, -10, -3))