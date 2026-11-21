# NUMBER GUESSING GAME
# This is practice for the AP Exam
# Purpose: an interactive which can entertain and test users loical and practical thinking skills
#Design: My program sets 3 different level prompts for the user which also has a difficulty level which the user can choose. Based on their input, a random number will generate wihthin the range given for the user to figure out.

import random
import time
def print_entrance_message(level_parameter):
    print("----------------------------------------")
    print(f"... Agent has locked in level {level_parameter} ")
    print("Iniciating seceret number")
    print("----------------------------------------")
    

def the_game():
    # keeps the game in one place

    # Variables
    levels = [1, 2, 3]
    
    choice_level= 0

    print("Welcome, agent, to the number guessing game")
    time.sleep(2)
    print("Your mission, should you choose to accept it, is to find the hidden digit in whatever milestone you choose")
    time.sleep(2)

    print("There are 3 milestones to this game")
    time.sleep(2)
    # INPUT 1 get the users level

    running= True
    while running:
        try:
            choice_level = int(input("Choose a level with numbers 1; easy, 2; medium, 3; Hard: "))
        except ValueError:
            print("Error: Please enter a valid number, not text!")
            continue
        if choice_level in levels:
             print("Great choice! Lets get started")
             running=False
        else:
            print("That is an invalid input. Please put in 1, 2, or 3:")
            continue
    running=False
    

    if choice_level == 1:
        secret_number = random.randint(1, 10)

        while True:
            try:
                user_guess = int(input("Scince this is level one, you will have to guess a number from 1 to 10:"))
            except ValueError: # <-- if there are any letters inputed by user, this will give a prompt saying it is an error
                print("Error: Please enter a valid number, not text!")
                continue
            if user_guess < secret_number:
                print("The number is greater")
            elif user_guess > secret_number:
                print("The number is less")
            elif user_guess == secret_number:
                print("YOU GOT IT!")
                break

    if choice_level == 2:
        secret_number = random.randint(1, 50)

        while True:
            try:
                user_guess = int(input("Now this is level 2. The number is from 1 to 50:"))
            except ValueError:
                print("Error: Please enter a valid number, not text!")
                continue
            if user_guess < secret_number:
                print("The number is greater")
            elif user_guess > secret_number:
                print("The number is less")
            elif user_guess == secret_number:
                print("YOU GOT IT!")
                break

    if choice_level == 3:
            secret_number = random.randint(1, 100)
    
            while True:
                try:
                    user_guess = int(input("You chose level 3. The hardest level! This is from 1 to 100!:"))
                except ValueError:
                    print("Error: Please enter a valid number, not text!")
                    continue
                if user_guess < secret_number:
                    print("The number is greater")
                elif user_guess > secret_number:
                    print("The number is less")
                elif user_guess == secret_number:
                    print("Congrats agent, you have solved the ")
                    break


print_entrance_message()
the_game()