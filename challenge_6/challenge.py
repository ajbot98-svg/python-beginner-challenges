# Home Work from GPT
# Challenge_6
# Rock, Paper, Scissors Game

import random

print("Welcome to Rock, Paper, Scissors Game!")

computer = random.choice(["rock", "paper", "scissors"])

player = input("Enter your choice (rock, paper, or scissors): ").lower()

print(f"Player chose: {player}")
print(f"Computer chose: {computer}")

# Check for invalid input
if player not in ["rock", "paper", "scissors"]:
    print("Invalid choice!")
else:
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("Computer wins!")

print("Thanks for playing!")
