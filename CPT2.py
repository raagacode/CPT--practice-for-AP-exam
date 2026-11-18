
# NUMBER GUESSING GAME
# This is practice for the AP Exam

import random
import time


def the_game():
    # Keeps the game in one place

    # Variables
    levels = [1, 2, 3]
    choice_level = 0

    print("Welcome to the number guessing game!")
    time.sleep(2)

    print("There are 3 levels to this game.")
    time.sleep(2)

    # INPUT 1: Get the user's level
    while choice_level not in levels:
        try:
            choice_level = int(input(
                "Choose your level:\n"
                "1 - Easy\n"
                "2 - Medium\n"
                "3 - Hard\n"
                "Enter your choice: "
            ))

            if choice_level in levels:
                print("Great choice! Let's get started!")
            else:
                print("Please enter 1, 2, or 3.")

        except ValueError:
            print("Please enter a number.")

    print("👇")

    # LEVEL 1: EASY
    if choice_level == 1:
        secret_number = random.randint(1, 10)

        while True:
            user_guess = int(input(
                "Since this is Level 1, guess a number from 1 to 10: "
            ))

            if user_guess < secret_number:
                print("The number is greater.")

            elif user_guess > secret_number:
                print("The number is less.")

            else:
                print("YOU GOT IT!")
                break

    # LEVEL 2: MEDIUM
    elif choice_level == 2:
        secret_number = random.randint(1, 50)

        while True:
            user_guess = int(input(
                "Now this is Level 2. Guess a number from 1 to 50: "
            ))

            if user_guess < secret_number:
                print("The number is greater.")

            elif user_guess > secret_number:
                print("The number is less.")

            else:
                print("YOU GOT IT!")
                break

    # LEVEL 3: HARD
    elif choice_level == 3:
        secret_number = random.randint(1, 100)

        while True:
            user_guess = int(input(
                "This is Level 3! Guess a number from 1 to 100: "
            ))

            if user_guess < secret_number:
                print("The number is greater.")

            elif user_guess > secret_number:
                print("The number is less.")

            else:
                print("YOU GOT IT!")
                break


# Start the game
the_game()
