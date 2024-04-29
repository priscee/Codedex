import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2

while True:
  guess = int(input("What is the total (2-12)? "))

  if guess != total:
    print("Try again.")
  else:
    print("Yay! You got it!")