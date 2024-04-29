import random

answer = input("Are we there yet? ")
ans = ['One more hour', 'Almost there', "Don't make me pullover"]

while answer != "yes":
  seleted_ans = random.choice(ans)
  print(seleted_ans)
  answer = input("Are we there yet? ")

if answer == "yes" or answer == "Yes":
  print("Okay")