my_fruits = {'🍓','🍒','🍎'}
friend_fruits = {'🫐','🍎','🍌'}

union_result = my_fruits.union(friend_fruits)
print(union_result)

intersection_result = my_fruits.intersection(friend_fruits)
print(intersection_result)

difference_result = my_fruits.difference(friend_fruits)
print(difference_result)

my_fruits.add('🍇')
print(my_fruits)

my_fruits.remove('🍎')
print(my_fruits)