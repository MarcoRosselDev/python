### 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

my_list = ['banana', 'orange', 'mango', 'lemon']
for_list =[]

for item in my_list:
    for_list.insert(0, item) 
    if len(for_list) == len(my_list):
        my_list = for_list
        print(my_list)

## comit
print("this is after for loop")
print(my_list)  # ['lemon', 'mango', 'orange', 'banana']