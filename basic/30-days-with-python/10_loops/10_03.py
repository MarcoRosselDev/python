# 3. Write a loop that makes seven calls to print(), so we get on 
# the output the following triangle:

"""  
#
##
###
####
#####
######
####### """

print('with for loop')
for a in list(range(1, 8)):
    print('#'*a)

print('with while loop')
count = 0
while count < 8:
    print('#'*count)
    count = count + 1

""" output 
with for loop
#
##
###
####
#####
######
#######

with while loop
#
##
###
####
#####
######
#######"""