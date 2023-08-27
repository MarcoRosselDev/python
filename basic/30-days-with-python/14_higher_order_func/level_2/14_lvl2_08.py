""" 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)) """

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

def upper(item):
    return item.upper()

def start_with_s_or_d_out(item):
    if item[0] == 'S' or item[0] == 'D':
        return False
    else:
        return True


sum_items = lambda a, b: a+b

chain_1 = list(filter(start_with_s_or_d_out, list(map(upper, countries))))

print(chain_1)