from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #List to keep track of the 3*3 board
        self.current_winner = None #Keep track of current winner
    
    def print_board(self):
        #This prints the rows
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        '''
            for (i, spot) in enumerate(self.board):
                moves = []
                if spot == ' ':
                    moves.append(i)
                
        '''

    def is_empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
        #return len(game.available_moves())
    
    def make_move(self, square, letter):
        #We check if the square is available and return True if it is else we will return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):

        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            #print("Won because of row")
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            #print("Won because of column")
            return True

        if square%2 == 0:
            diagnol1 = [ self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagnol1]):
                #print("Won because of diag1")
                return True

            diagnol2 = [ self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagnol2]):
                #print("Won because of diag2")
                return True
        
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'

    while game.is_empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move in square {square}')
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!!')
                return letter

            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.8)
    
    if print_game:        
        print('It is a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
