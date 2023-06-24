import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    letters_in_word = set(word) #To find a set of all the letters
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    while len(letters_in_word) > 0:

        #Display the used letters
        print('You have used these: ' + ' '.join(used_letters))

        #User guessing a input
        user_input_letter = input('Guess a letter: ')

        #Display the letters in the word
        letter_list = [ letter if letter in used_letters else '-' for letter in word]
        print('The letters in the words: ' + ' '.join(letter_list))

        if user_input_letter in alphabet - used_letters:
            used_letters.add(user_input_letter)
            if user_input_letter in letters_in_word:
                letters_in_word.remove(user_input_letter)
        elif user_input_letter in used_letters:
            print('The letter is already in used letters. Please try again')
        else:
            print('The character is invalid. Please try again')
    
    #Reached here since letters_in_word is 0
    print("Congrats!! The word is: "+ word)

hangman()