
from art import logo
import random as re

def guess_game():
    counter = 0
    print(logo)
    print("Welcome to the number guessing game!\n")
    print("I am thinking of a number between 1 and 100.")
    #Computer has a random number saved
    number = re.randint(1,100)
    #Selecting difficulty
    difficulty = (input("Do you want to play on easy or hard mode?\n")).lower() #local scope
    #Setting counter
    if difficulty == 'easy':
        counter = 10
        print(f"You have {counter} tries to guess")
    elif difficulty == 'hard':
        counter = 5
        print(f"You have {counter} tries to guess")
    elif difficulty != 'easy' or difficulty != 'hard':
        print("You didn't select the correct option, select between easy or hard\n")
        return None
    #2 conditions for game to contniue
    won = False
    while won == False:
        guess = int(input('Guess a number\n'))
        if guess == number:
            print("You have guessed right!! Congratulations!!")
            won = True
        elif guess < number:
            counter -= 1
            print('Go higher, you guessed too low!')
            print(f"You have {counter} tries to guess")
        elif guess > number:
            counter -= 1
            print('Go lower, you guessed too high!')
            print(f"You have {counter} tries to guess")
        if counter < 1:
            won = True

play = (input("Do you want to play a guessing game? y or n\n")).lower()
while play == 'y':
    guess_game()
    play = (input("Do you want to play another game? y or n\n")).lower()
    if play == 'y':
        print('\n'*100)






