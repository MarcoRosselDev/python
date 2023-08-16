### 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_lt = ('apple', 'pear', 'strawberry', 'tomato', 'potato', 'broccoli', 'pig', 'chiken', 'cow')
print( 'len of food stuff it tuple : ', len(food_stuff_lt))
# len of food stuff it tuple :  9
food_stuff_lt = list(food_stuff_lt)
del food_stuff_lt[4]
food_stuff_lt = tuple(food_stuff_lt)
print(food_stuff_lt)
# ('apple', 'pear', 'strawberry', 'tomato', 'broccoli', 'pig', 'chiken', 'cow')