### 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

# sprint = April - June
# summer = July - September
# autumn, fall = October - December
# winter = January - March
def check_season(month):
    if type(month) == str:
        if month == 'April' or month == 'May' or month == 'June':
            print(f'in {month} we are in Sprint')
        elif month == 'July' or month == 'August' or month == 'September':
            print(f'in {month} we are in Summer')
        elif month == 'October' or month == 'November' or month == 'December':
            print(f'in {month} we are in Autumn')
        elif month == 'April' or month == 'February' or month == 'March':
            print(f'in {month} we are in Winter')
        else:
            print(f'{month} is not a valid string \n please capitalize the month \n like = March, not march')
    else:
        print('please capitalize the month')

#
check_season('march')
check_season('March')

""" output:
march is not a valid string 
 please capitalize the month 
 like = March, not march
in March we are in Winter """