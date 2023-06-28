import random
import re

#Create the board object
#So that we can perform the operations using this object - like create or show the board

class Board:
    def __init__(self, dim_size, num_of_bombs):
        #storing the parameters into the object so that we can use them in a later time
        self.dim_size = dim_size
        self.num_of_bombs = num_of_bombs

        #Let's create the board
        #helper function
        self.board = self.make_new_board()

        self.assign_values_to_board()

        #initialize a set that keeps in store the locations that have been dug.
        #For example if (0,0) is dug, then self.dug = ((0,0))
        self.dug = set()
    
    def make_new_board(self):
        #Create a board variable that is in dim_size * dim_size dimensions
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_count = 0

        while bombs_count < self.num_of_bombs :
            #We are finding a random integer between 0 and dim_size**2 which is the number of cells in the board.
            #We find the row index by dividing by the dimension and we find the column index by finding the cell
            #that is present after choosing the specific row_index
            bombs_random_factor = random.randint(0, self.dim_size**2 -1 )
            row = bombs_random_factor // self.dim_size
            col = bombs_random_factor % self.dim_size

            #If the particular spot, already consists of a bomb then we skip the particular spot as we do not
            # want to over write it
            #If the spot is free or empty we initialize it with * indicating a bomb
            if board[row][col] == '*' :
                continue
            else:
                board[row][col] = '*'
                bombs_count += 1
        
        return board
    
    def assign_values_to_board(self):
        #We iterate through the board and then assign the number of neighbouring bombs to each index.
        for r in range(0, self.dim_size):
            for c in range(0, self.dim_size):
                #if the location is a bomb, then we ignore
                if self.board[r][c] == '*':
                    continue
                else:
                    #We find the number of neigbouring bombs, if the location is not a bomb and then set
                    #the value to it
                    self.board[r][c] = self.get_number_of_neighboring_bombs(r, c)
    
    def get_number_of_neighboring_bombs(self, row, col):

        #We need to check the following surrounding indices:
        #Top Left: (row-1, col-1)
        #Top Center: (row-1, col)
        #Top Right: (row-1, col+1)
        #Left: (row, col-1)
        #Right: (row, col+1)
        #Bottom Left: (row+1, col-1)
        #Bottom Center: (row+1, col)
        #Bottom Right: (row+1, col+1)

        num_of_neigbour_bombs = 0

        #Iterate through the neighboring cells
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1 ):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1) + 1 ):
                #We are skipping the count for the original location
                if r == row and c == col:
                    continue
                else:
                    if self.board[r][c] == '*':
                        num_of_neigbour_bombs += 1
        
        return num_of_neigbour_bombs
                
    def dig(self, row, col):

        #If the particular location (row, col) has a bomb, then we return False
        #If the location does not have a bomb and has a number, then we return True
        #If the location is blank, then we return True but before that we recursively dig our nearby cells

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        if self.board[row][col] > 0:
            return True
        #if (row, col) in self.dug:
        #    return True
     
        
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) + 1):
            for c in range( max(0, col-1), min(self.dim_size-1, col+1) + 1):
                if (r,c) in self.dug: #Don't dig where you already dug
                    continue
                self.dig(r, c)
        
        return True

    def __str__(self):
        #Now print and show the user the board and it's values
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep 

#play the game
def play(dim_size=10, num_of_bombs=10):
    #Step 1 - Create the board and plant the bombs
    board = Board(dim_size, num_of_bombs)
    #Step 2 - Show the board to user and ask him where he wants to dig
    #Step 3a - If the location is a bomb, convey to him he lost and that the game is over
    #Step 3b - If the location is a blank space, then the user can recursively choose another spot to dig
    #Step 4 - Repeat the steps 2-> 3a/b until there is no other space to dig -> Victory
    
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_of_bombs:
        print(board)

        #Get user input
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as (row, col)"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row<0 or row>=dim_size or col<0 or col>=dim_size:
            print("Invalid location chosen. Please try again")
            continue

        #If it is valid, then dig
        safe = board.dig(row, col)

        if not safe:
            #You dug a bomb
            print("Sorry a mine has blew. Game is over.")
            break
    
    if safe:
        print("Hurray! you have won the game")
    else:
        #If you have encountered a mine, then Let's reveal the entire board
        board.dug = [(r,c) for r in range(0, dim_size) for c in range(0, dim_size)]   
        print(board)     

if __name__ == '__main__':
    play()