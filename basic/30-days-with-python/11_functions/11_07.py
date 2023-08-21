""" 7. Quadratic equation is calculated as follows: 
ax² + bx + c = 0. Write a function which calculates 
solution set of a quadratic equation, solve_quadratic_eqn.
"""

def solve_quadratic_eqn():
    a = float(input('please enter [a] value of ax² + bx + c = 0 : '))
    b = float(input('please enter [b] value of ax² + bx + c = 0 : '))
    c = float(input('please enter [c] value of ax² + bx + c = 0 : '))
    comprub = (b*b - 4*a*c)
    if comprub > 0:
        solution_less_b = (-b - (b*b - 4*a*c)*1/2)/2*a
        solution_plus_b = (-b + (b*b - 4*a*c)*1/2)/2*a
        print(f'This are two soluctions: \n {solution_less_b} and {solution_plus_b}')
    else:
        print('No soluction')

solve_quadratic_eqn()

""" output:
please enter [a] value of ax² + bx + c = 0 : 3
please enter [b] value of ax² + bx + c = 0 : 5
please enter [c] value of ax² + bx + c = 0 : 2
This are two soluctions: 
 -8.25 and -6.75 """