def get_item(a):
  if a == 1:
    return '🍔 Cheeseburger' 
  elif a == 2:
    return '🍟 Fries'
  elif a == 3:
    return '🥤 Soda'
  elif a == 4:
    return '🍦 Ice Cream'
  elif a == 5:
    return '🍪 Cookie'
  else:
    return 'invalid'

def welcome():
  print("Welcome to McDonald's Drive-Thru")
  print('\n')
  print("Menu:")
  print('1. 🍔 Cheeseburger')
  print('2. 🍟 Fries')
  print('3. 🥤 Soda')
  print('4. 🍦 Ice Cream')
  print('5. 🍪 Cookie')
  print('\n')

welcome()

option = int(input("What would you like to order? "))
print('\n')
print(get_item(option))