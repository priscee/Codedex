import random 

#===Rules===#
print("Rock Paper Scissors\n")
print("Rules:")
print("Rock beats Scissors.\n"
    + "Scissors beat Paper.\n"
    + "Paper beats Rock.\n")

#===Player===#
print("1 = ✊ Rock")
print("2 = 🖐️ Paper")
print("3 = ✌️ Scissors")
print("\n")
player =int(input("Pick a number: "))

print("\n")

if player == 1:
    print("Player: ✊")
elif player == 2:
    print("Player: 🖐️")
else:
    print("Player: ✌️")

#===Computer===#
computer = random.randint(0, 3)

if computer == 1:
    print("Computer: ✊")
elif computer == 2:
    print("Computer: 🖐️")
else:
    print("Computer: ✌️")

print("\n")

#===Tie===#
if player == computer:
    print("Tie!")

#===Winning/Losing Conditions===#
if player == 1 and computer == 3:
    print("You won!")
elif player == 1 and computer == 2:
    print("You lose!")

if player == 2 and computer == 1:
    print("You won!")
elif player == 2 and computer == 3:
    print("You lose!")

if player == 3 and computer == 2:
    print("You won!")
elif player == 3 and computer == 1:
    print("You lose!")

print("\n")

#===End===#
print("Thanks for playing!\n")