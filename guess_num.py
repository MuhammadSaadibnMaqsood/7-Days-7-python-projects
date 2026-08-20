import random

def guess_num():
    system_num = random.randint(0,9)
    print("WELCOME TO THE GUESSING NUMBER")
    print("-------------------------------")
    while True:
        user_num = int(input("Enter your guess (0-9): "))
        if(system_num == user_num):
            print("YOU WON")
            break
        else:
            print("YOU GUESS WRONG")
            
        
guess_num()