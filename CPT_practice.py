#  NUMBER GUESSING GAME
# This is practice for the AP Exam

import random

def the_game(): # keeps the game in one place
    
    levels=[" 1", " 2", " 3"]
levels=[" 1", " 2", " 3"]


print("Welcome to the number guessing game!")

print("There are 3 levels to this game")
# INPUT 1 get the users level

choice_level = input('Choose your level with numbers 1, easy, 2, medium, 3, Hard:').lower()

if choice_level not in levels:
    print("Please pick a level from 1, 2, and 3")
else:
    print("Great choice! Lets get started!")
