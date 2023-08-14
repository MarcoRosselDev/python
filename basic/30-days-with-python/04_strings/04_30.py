### 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
challenge = '   Coding For All      '
solution = challenge.strip(' ')
print(solution)
# Coding For All

""" 31. Which one of the following variables return True when we use the method isidentifier():
    30DaysOfPython
    thirty_days_of_python 
"""

first_var = '30DaysOfPython'
second_var = 'thirty_days_of_python'

ident_first_var = first_var.isidentifier()
ident_second_var = second_var.isidentifier()
print('30DaysOfPython ? : ',ident_first_var)
# 30DaysOfPython ? :  False <----- because it started with a number
print('thirty_days_of_python ? : ',ident_second_var)
# thirty_days_of_python ? :  True