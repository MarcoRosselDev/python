### 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('apple', 'pear', 'strawberry')
vegetables = ('tomato', 'potato', 'broccoli')
animals = ('pig', 'chiken', 'cow')
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
# ('apple', 'pear', 'strawberry', 'tomato', 'potato', 'broccoli', 'pig', 'chiken', 'cow')

### 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
print(type(food_stuff_tp)) # <class 'list'>