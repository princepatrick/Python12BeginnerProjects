import math 
import random 

class Player:
    def __init__(self, letter):
        #The letter is x or o
        self.letter = letter
    
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        #The computer selects a square in a random fashion
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            val = input('Enter a number from 1-9: ')
            
            try:
                val = int(val)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('The value is invalid. Please try again')
        
        return val

