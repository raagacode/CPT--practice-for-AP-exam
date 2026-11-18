#  NUMBER GUESSING GAME
# This is practice for the AP Exam

import random
import time
# Variables

levels=[ 1,  2,  3]

choice_level = "" 

def the_game(): # keeps the game in one place
    while running:
        print("Welcome to the number guessing game!")
        time.sleep(2)
   
        print("There are 3 levels to this game")
   # INPUT 1 get the users level
        time.sleep(2)
    print("Welcome to the number guessing game!") 
    time.sleep(1)
    print("There are 3 levels to this game")
    time.sleep(1)
    running = True


    if choice_level != "1" or choice_level != "2" or choice_level != "3":
        choice_level = int(input("Choose your level with numbers 1; easy, 2; medium, 3; Hard: "))
   
    if choice_level in levels:
        print("Great choice! Lets get started")
    else:
        input("Please put in 1, 2, or 3:")
    if input == levels:
        print('Good choice! Lest start!') 
    print("👇")
    running = False
    return 


if choice_level == 1:
        secret_number = random.randint(1, 10)
while True:
        user_guess =  int(input("Since this is level one, you have to guess a number from 1 to 10:"))
        if user_guess < secret_number:
            print("The number is greater")
        elif user_guess > secret_number:
            print("The number is less")
        elif user_guess == secret_number:
            print("YOU GOT IT!")    
        break


if choice_level == 2:
        secret_number1 = random.randint(1, 50)

while True:
        user_guess2 = int(input("Choose a random number between 1 and 50:"))

        if user_guess2 < secret_number1:
            print("The number is greater")
        elif user_guess2 > secret_number1:
            print("The number is less")
        elif user_guess2 == secret_number1:
            print("YOU GOT IT!")
            break
    

   
if choice_level == 3:
    secret_number2 = random.randint(1, 100)

    while True:
        user_guess3 = int(input("Choose a random number between 1 and 100:"))

        if user_guess3 < secret_number2:
            print("The number is greater")
        elif user_guess3 > secret_number2:
            print("The number is less")
        elif user_guess3 == secret_number2:
            print("YOU GOT IT!")
            break

#create a main() function, to get the game started. run the_game() from within main(). return final message


