import random

print("================================")
print("     ROCK PAPER SCISSORS")
print("================================")

choices = ["rock", "paper", "scissors"]

while True:

    # Get player's choice
    player = input("\nEnter rock, paper, scissors (or quit): ").lower()

    if player == "quit":
        print("Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Computer chooses randomly
    computer = random.choice(choices)

    print("You chose     :", player)
    print("Computer chose:", computer)

    # Decide winner
    if player == computer:
        print("Result: DRAW!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("Result: YOU WIN! 🎉")

    else:
        print("Result: COMPUTER WINS! 🤖")

print("\nGame Over!")
