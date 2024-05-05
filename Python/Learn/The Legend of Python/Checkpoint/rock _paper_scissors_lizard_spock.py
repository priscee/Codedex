import random 

#===Rules===#
print("Rock Paper Scissors Lizard Spock\n")
print("Rules:")
print("Scissors cut Paper\n"
    + "Paper covers Rock\n"
    + "Rock crushes Lizard\n"
    + "Lizard poisons Spock\n"
    + "Spock smashes Scissors\n"
    + "Scissors beat Lizard\n"
    + "Lizard eats Paper\n"
    + "Paper disproves Spock\n"
    + "Spock vaporizes Rock\n"
    + "Rock breaks Scissors\n"
    )

#===Player===#
print("1 = ✊ Rock")
print("2 = 🖐️ Paper")
print("3 = ✌️ Scissors")
print("4 = 🦎 Lizard")
print("5 = 🖖 Spock")
print("\n")
player =int(input("Pick a number: "))

print("\n")

if player == 1:
    print("Player: ✊")
elif player == 2:
    print("Player: 🖐️")
elif player == 3:
    print("Player: ✌️")
elif player == 4:
    print("Player: 🦎")
else:
    print("Player: 🖖")

#===Computer===#
computer = random.randint(1, 5)

if computer == 1:
    print("Computer: ✊")
elif computer == 2:
    print("Computer: 🖐️")
elif computer == 3:
    print("Computer: ✌️")
elif computer == 4:
    print("Computer: 🦎")
else:
    print("Computer: 🖖")

print("\n")

#===Tie===#
if player == computer:
    print("Tie!")

#===Winning/Losing Conditions===#
#player = 1 ✊
if player == 1 and computer == 2:
    print("You Lose! You got covered!")
elif player == 1 and computer == 3:
    print("You Win! You broke scissors!")
elif player == 1 and computer == 4:
    print("You Win! You crushed Lizard!")
elif player == 1 and computer == 5:
    print("You Lose! You got vaporized!")

#player = 2 🖐️
if player == 2 and computer == 1:
    print("You Win! You covered rock!")
elif player == 2 and computer == 3:
    print("You Lose! You got cut!")
elif player == 2 and computer == 4:
    print("You Lose! You got eaten!")
elif player == 2 and computer == 5:
    print("You Win! You disproved spock!")

#player = 3 ✌️
if player == 3 and computer == 1:
    print("You Lose! You got broken!")
elif player == 3 and computer == 2:
    print("You Won! You cut paper!")
elif player == 3 and computer == 4:
    print("You Won! You beat lizard!")
elif player == 3 and computer == 5:
    print("You Lose! You got smashed!")

#player = 4 🦎
if player == 4 and computer == 1:
    print("You Lose! You got crushed!")
elif player == 4 and computer == 2:
    print("You Win! You ate paper!")
elif player == 4 and computer == 3:
    print("You Lose! You got beaten!")
elif player == 4 and computer == 5:
    print("You Win! You poisoned spock!")

#player = 5 🖖
if player == 5 and computer == 1:
    print("You Win! You vaporized rock!")
elif player == 5 and computer == 2:
    print("You Lose! You got disproved!")
elif player == 5 and computer == 3:
    print("You Win! You smashed scissors!")
elif player == 5 and computer == 4:
    print("You Lose! You got poison!")

print("\n")

#===End===#
print("Thanks for playing!\n")