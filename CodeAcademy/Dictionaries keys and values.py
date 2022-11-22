import time
groceries = {
'fruits': ['mangoes', 'bananas', 'apples'],
'protein': ['beef', 'pork', 'salmon'], 
'carbs': ['rice', 'pasta', 'bread'],
'veggies': ['lettuce', 'cabbage', 'onions']
}
time.sleep(0.5)
print(groceries['veggies'])

second_list = {'desserts': ['rice pudding', 'ice cream', 'cake']}
groceries.update(second_list)
time.sleep(1)
print(groceries)
time.sleep(0.5)
print(groceries.keys())
time.sleep(0.5)
print(groceries.values())


