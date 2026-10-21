# Rock Paper Scissors Game
import random

# Define the choices and their corresponding emojis
choices = ["r", "p", "s"]
emojis = {"r": "🪨", "p": "📄", "s": "✂️"}

while True:
    # Get the user's choice
    user_choice = input("Enter your choice (r,p,s) : ").lower().strip()
    if user_choice not in choices:
        print("Invalid Choice")
        continue

    # Get the computer's choice
    computer_choice = random.choice(choices)

    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "p" and computer_choice == "r")
        or (user_choice == "s" and computer_choice == "p")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    # Ask the user if they want to play again
    play_again = input("Continue? (y/n): ").lower()

    if play_again == "n":
        print("Thanks for playing!")
        break
