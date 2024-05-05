import random

symbols = ['🍒','🍇','🍉','7️⃣']

'''
results = random.choices(symbols, k=3)

print(f"{results[0]} | {results[1]} | {results[2]}")

if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣')
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")
'''
#-------#
'''Bonus'''

def play():

  for i in range(1, 6): #6: number of jackput lines to be printed out
    results = random.choices(symbols, k = 3)
    print(f"{results[0]} | {results[1]} | {results[2]}")
    jackpot = results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'

    if jackpot:
      print("Jackpot! 💰")
    else:
      results = random.choices(symbols, k=3)
  
next_round = ''
while next_round.upper != 'N':
  play()
  next_round = input('Keep playing? (Y/N): ')

print("Thanks for playing!")