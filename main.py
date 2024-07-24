import random
from replit import clear
HARD = 5
EASY = 10


def again():
    game_again = input("Do you want to play this game again: Type 'YES' or 'NO': ").lower()
    if game_again == 'yes':
        clear()
        return game()
    elif game_again == 'no':
        print("GOOD LUCK")
        return


def checking(guess, computer, setting):
    if guess > computer:
        print("This number is bigger.")
        return setting - 1
    elif guess < computer:
        print("This number is smaller.")
        return setting - 1
    elif guess == computer:
        print("...YOU WIN...")
        return


def set_level():
    game_level = input("PLease choose game level: Type for Hard 'YES' and for easy 'NO': ").lower()
    if game_level == 'yes':
        return HARD
    elif game_level == 'no':
        return EASY


def game():
    print("Welcome to the computer guessing game.")
    print("This mission is very friendly..")
    setting = set_level()
    computer = random.randint(0, 99)
    print(f"This answer is: {computer}")
    guess = 0
    while computer != guess:
        print(f"You have this {setting} amount of time to play.")
        guess = int(input("Make guess more: "))
        setting = checking(guess, computer, setting)
        if setting == 0:
            print("...YOU LOST...")
            return again()
game()
