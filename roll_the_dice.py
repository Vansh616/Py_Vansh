import random

# Ask the user if they want to roll the dice
a = input("Roll the dice? (y/n): ").lower()

# if user says yes, roll the dice
while a == "y":
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}.")
    a = input("Roll the dice again? (y/n): ").lower()

    # if user says no, exit the loop
    if a != "y":
        print("Thanks for playing!")
        break

print("Goodbye!")
