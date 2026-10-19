import random

# Ask the user if they want to roll the dice
a = input("Roll the dice? (y/n): ").lower()

# if user says yes, roll the dice
while a == "y":
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}.")
    a = input("Roll the dice again? (y/n): ").lower()

    # if user says no, exit the loop
    if a == "n":
        print("Hope we see you again!!")
        break
    elif a != "y" or a != "n":
        print("Thanks for playing!")
        break
    
print("Goodbye!")
