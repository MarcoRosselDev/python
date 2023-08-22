# 4. Write a function which check if provided variable is a valid python variable

def check_valid_variable(name):
    if type(name[0]) == int:
        print('invalid variable name, it start with a number')
        # I continued tomorrow