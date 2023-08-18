""" 2. Check if the season is Autumn, Winter, Spring or Summer. If the user 
input is: September, October or November, the season is Autumn. December, 
January or February, the season is Winter. March, April or May, the season is 
Spring June, July or August, the season is Summer
"""

month = input('Plsase enter the month : ')

if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer')
else:
    print('please write the month correctly, like : November, not : november /n starting with mayuscule')