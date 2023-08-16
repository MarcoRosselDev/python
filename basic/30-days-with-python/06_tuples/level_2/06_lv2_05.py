### 5. Slice out the first three items and the last three items from food_staff_lt list

food_stuff_lt = ('apple', 'pear', 'strawberry', 'tomato', 'potato', 'broccoli', 'pig', 'chiken', 'cow')

food_stuff_lt = list(food_stuff_lt)

food_stuff_lt = food_stuff_lt[3:6]
print(food_stuff_lt)
# ['tomato', 'potato', 'broccoli']

food_stuff_lt = tuple(food_stuff_lt)
print(food_stuff_lt)
# ('tomato', 'potato', 'broccoli')
