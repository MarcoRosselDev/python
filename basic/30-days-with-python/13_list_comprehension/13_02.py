## 13. Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

one_d_list = [num for box in list_of_lists for num in box ]
print(one_d_list)

a = [box for box in list_of_lists for num in box  for box  in num ] 
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# no se como lo logre pero ahi esta