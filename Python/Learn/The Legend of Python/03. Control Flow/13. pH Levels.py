ph = int(input('Enter pH value: '))

if ph > 7:
  print('Basic')
elif ph < 7:
  print('Acidic')
else:
  print('Neutral')