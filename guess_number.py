#A game to guess the number. The code will ask you to try again until you guess it right.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while guess != random_number :
        guess = int(input(f"Guess a number between 1 and {x}: "))
        
        if guess < random_number :
            print("The guess is incorrect. Too low")
        elif guess > random_number :
            print("The guess is incorrect. Too high")
    
    print(f"You guessed it!!!. The secret number is {guess} ")

guess(15)