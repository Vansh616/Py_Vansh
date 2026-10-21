# Number Guessing Game
import random

# Function to guess a number between 1 and x
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    # Keep asking the user to guess until they get it right
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry, guess again. Too low.")

        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay! Congrats. You have guessed the number {random_number} correctly!")
    
guess(100)
