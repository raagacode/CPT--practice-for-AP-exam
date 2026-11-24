

import random
import time
def print_entrance_message(choice_level):
    print("----------------------------------------")
    print(f"... Agent has locked in level {choice_level} ")
    print("Iniciating level sequence")
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(1)
    print("----------------------------------------")
    time.sleep(1)
    

def the_game():



    
    levels = [1, 2, 3]
    
    choice_level= 0

    print("𝕎𝕖𝕝𝕔𝕠𝕞𝕖, 𝕒𝕘𝕖𝕟𝕥, 𝕥𝕠 𝕥𝕙𝕖 𝕟𝕦𝕞𝕓𝕖𝕣 𝕘𝕦𝕖𝕤𝕤𝕚𝕟𝕘 𝕘𝕒𝕞𝕖")
    time.sleep(2)
    print("𝕐𝕠𝕦𝕣 𝕞𝕚𝕤𝕤𝕚𝕠𝕟, 𝕤𝕙𝕠𝕦𝕝𝕕 𝕪𝕠𝕦 𝕔𝕙𝕠𝕠𝕤𝕖 𝕥𝕠 𝕒𝕔𝕔𝕖𝕡𝕥 𝕚𝕥, 𝕚𝕤 𝕥𝕠 𝕗𝕚𝕟𝕕 𝕥𝕙𝕖 𝕙𝕚𝕕𝕕𝕖𝕟 𝕕𝕚𝕘𝕚𝕥 𝕚𝕟 𝕨𝕙𝕒𝕥𝕖𝕧𝕖𝕣 𝕞𝕚𝕝𝕖𝕤𝕥𝕠𝕟𝕖 𝕪𝕠𝕦 𝕔𝕙𝕠𝕠𝕤𝕖")
    time.sleep(2)

    print("𝕋𝕙𝕖𝕣𝕖 𝕒𝕣𝕖 3 𝕞𝕚𝕝𝕖𝕤𝕥𝕠𝕟𝕖𝕤 𝕥𝕠 𝕥𝕙𝕚𝕤 𝕘𝕒𝕞𝕖e")
    time.sleep(2)

    running= True
    while running:
        try:
            choice_level = int(input("ᴄʜᴏᴏꜱᴇ ᴀ ʟᴇᴠᴇʟ ᴡɪᴛʜ ɴᴜᴍʙᴇʀꜱ 1; ᴇᴀꜱʏ, 2; ᴍᴇᴅɪᴜᴍ, 3; ʜᴀʀᴅ: "))
        except ValueError:
            print("Error: Please enter a valid number, not text!")
            continue # this loops the code 
        if choice_level in levels:
             print("Great choice! Lets get started")
             print_entrance_message(choice_level)
             running=False
        else:
            print("That is an invalid input. Please put in 1, 2, or 3:")
            
            print_entrance_message(choice_level)
            continue
    running=False
    

    if choice_level == 1:
        secret_number = random.randint(1, 10)

        while True:
            try:
                user_guess = int(input("Scince this is level one, you will have to guess a number from 1 to 10. Guess your number:"))
            except ValueError: # <-- if there are any letters inputed by user, this will give a prompt saying it is an error
                print("Error: Please enter a valid number, not text!")
                continue
            if user_guess < secret_number:
                print("The number is greater")
            elif user_guess > secret_number:
                print("The number is less")
            elif user_guess == secret_number:
                print("Congrats agent, you have solved the case!👍")
                break

    if choice_level == 2:
        secret_number = random.randint(1, 50)

        while True:
            try:
                user_guess = int(input("Now this is level 2. The number is from 1 to 50. Guess your number:"))
            except ValueError:
                print("Error: Please enter a valid number, not text!")
                continue
            if user_guess < secret_number:
                print("The number is greater")
            elif user_guess > secret_number:
                print("The number is less")
            elif user_guess == secret_number:
                print("Congrats agent, you have solved the case!👍")
                break

    if choice_level == 3:
            secret_number = random.randint(1, 100)
    
            while True:
                try:
                    user_guess = int(input("You chose level 3. The hardest level! This is from 1 to 100!. Guess your number:"))
                except ValueError:
                    print("Error: Please enter a valid number, not text!")
                    continue
                if user_guess < secret_number:
                    print("The number is greater")
                elif user_guess > secret_number:
                    print("The number is less")
                elif user_guess == secret_number:
                    print("Congrats agent, you have solved the case!👍")
                    break



the_game()





