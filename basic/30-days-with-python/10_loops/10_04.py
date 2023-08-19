### 4. Use nested loops to create the following:

""" 
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #     es un 8 x 8 (#)"""

# bucles anidados ->

for fila in range(0, 8):
    for mult in range(0, 9):
        column = ('# '*mult)
    print(column)

""" output
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # 
# # # # # # # # """