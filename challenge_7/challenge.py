# Home Work Challenge:
# Challenge_7
# Number Guessing Game.

import random

print("Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0

    guess = None
    while guess != secret_number:
        guess = int(input("Please enter your guess (1-100): "))
        attempts += 1

        if guess < secret_number:
            print ("Too Low!")
        elif guess > secret_number:
            print ("Too High!")
        else:
            print (f"congratulations! You guessed it in {attempts} attempts.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print("Thank you for playing! Goodbye!")
        break