# Rock Paper Scissors Game
import random

# Define the choices and their corresponding emojis
choices = ["r", "p", "s"]
emojis = {"r": "🪨", "p": "📄", "s": "✂️"}


# Function to get the user's choice
def get_user_choice():
    while True:
        # Get the user's choice
        user_choice = input("Enter your choice (r,p,s) : ").lower().strip()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please enter 'r', 'p', or 's'.")


# Function to display the choices
def display_choices(user_choice, computer_choice):
    print(f"You chose: {emojis[user_choice]}")
    print(f"Computer chose: {emojis[computer_choice]}")


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
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


# Function to play the game
def play_game():

    while True:
        user_choice = get_user_choice()

        # Get the computer's choice
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        # Ask the user if they want to play again
        play_again = input("Continue? (y/n): ").lower().strip()

        if play_again == "n":
            print("Thanks for playing!")
            break


play_game()
