list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for fila in list_of_lists for number in fila]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]