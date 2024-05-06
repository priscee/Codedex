# Write code below 💖

import random

def fortune():
  fortune = random.randint(1, 7)

  if fortune == 1:
    print("Don't pursue happiness – create it.")
  elif fortune == 2:
    print("All things are difficult before they are easy.")
  elif fortune == 3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif fortune == 4:
    print("Someone in your life needs a letter from you.")
  elif fortune == 5:
    print("Don't just think. Act!")
  elif fortune == 6:
    print("Your heart will skip a beat.")
  elif fortune == 7:
    print("The fortune you search for is in another cookie.")
  else:
    print("Help! I'm being held prisoner in a Chinese bakery!")

fortune()