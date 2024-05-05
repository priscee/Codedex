print("Sorting Hat 🪄")

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Sorting House\n")

#===Question 1===#
print('Q1) Do you like Dawn or Dusk?\n')
print('\t1) Dawn\n')
print('\t2) Dusk\n')
answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin +=1
else:
  print('Wrong input.')

#===Question 2===#
print("\nQ2) When I'm dead, I want people to remeber me as:\n")
print('\t1) The Good\n')
print('\t2) The Great\n')
print('\t3) The Wise\n')
print('\t4) The Bold\n')
answer = int(input('Enter answer (1-4): '))

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

#===Question 3===#
print('\nQ3) Which kind of instrucment most pleases your ear?\n')
print('\t1) The violin\n')
print('\t2) The trumpet\n')
print('\t3) The piano\n')
print('\t4) The drum\n')
answer = int(input('Enter answer (1-4): '))

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')

#===Sort===#

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
  print('\n🦁 Gryffindor!')
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
  print('\n🦅 Ravenclaw!')
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
  print('\n🦡 Hufflepuff!')
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
  print('\n🐍 Slytherin!')