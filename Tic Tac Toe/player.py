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

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if game.num_empty_squares == 9:
            square = random.choice(game.available_moves())
            return square
        else:
            square = self.minimax(game, self.letter)['position']
            return square
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position':None, 'score': 1 * (state.num_empty_squares()+1) if other_player == max_player else -1 * (state.num_empty_squares()+1) }
        elif not state.num_empty_squares():
            return {'position':None, 'score':0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position':None, 'score': math.inf}
        
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)

            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        
        return best


