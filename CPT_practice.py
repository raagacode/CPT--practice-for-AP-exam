#  NUMBER GUESSING GAME
# This is practice for the AP Exam

import random

def the_game(): # keeps the game in one place

    levels=[ 1, 2,  3]
levels=[ 1,  2,  3]


print("Welcome to the number guessing game!")

print("There are 3 levels to this game")
# INPUT 1 get the users level

choice_level = ""

running = True

while running: 
    
    if choice_level != "1" or choice_level != "2" or choice_level != "3":
     choice_level = int(input("Choose your level with numbers 1; easy, 2; medium, 3; Hard: "))

    if choice_level in levels:
        print("Great choice! Lets get started")
    else:
        input("Please put in 1, 2, or 3:")
    if input is levels:
       print('Good choice! Lest start!')
    
    running = False 

    

