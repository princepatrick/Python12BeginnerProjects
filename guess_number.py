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

def computer_guess(n):
    low = 0
    high = n
    feedback = ''
    
    while feedback != 'C':
        guess = random.randint(low, high)
        
        feedback = input(f"The computers's guess is {guess}. Please respond if it is High (H) or Low (L) or Correct (C) : " )
        
        if feedback == 'H':
            high = guess-1
        elif feedback == 'L':
            low = guess+1
    
    print(f'Congratulations computer, You have found the number, {guess}')

guess(15)
computer_guess(1000)