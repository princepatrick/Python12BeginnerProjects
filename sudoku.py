def find_next_empty(puzzle):
    #print(f'Attempting find_next_empty')
    for r in range(9):
        for c in range(9):
            #print(puzzle[r][c])
            if puzzle[r][c] == -1:
                #print(f'Need to return {r} {c}')
                return r, c 
    #print(f'Need to return None')
    return 300, 300

def is_valid(guess, puzzle, row, col):
    #Check if the row vals, col vals and 3*3 matix if the guess is present already 
    #return False or else return True

    #print(f'is_valid() with {row} and {col} and guess is {guess}')

    row_vals = puzzle[row]

    if guess in row_vals:
        #print(f'{guess} and {row_vals}')
        return False

    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])

    if guess in col_vals:
        #print(f'{guess} and {col_vals}')
        return False
    
    row_start = row // 3
    col_start = col // 3

    #print(f'Going to check for {row_start},{col_start} to {row_start+3},{col_start+3}')

    for r in range(row_start*3, row_start*3+3):
        for c in range(col_start*3, col_start*3+3):
            if puzzle[r][c] == guess:
                return False
    
    #print(f'{row} {col} is valid')
    return True
        
def solve_sudoku(puzzle):
    #print(f'Attempted')
    row, col = find_next_empty(puzzle)

    #print(f'{row} {col}')
    if row == 300:
        #print(puzzle)
        return True

    for guess in range(1, 10):
        if is_valid(guess, puzzle, row, col):
            #print(f'{guess} tried in {row} and {col}')
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1
    
    return False

if __name__ == '__main__':
    example_board = [[5,1,6,8,2,7,9,4,3],[2,7,8,3,9,4,6,1,5],[3,4,9,6,1,5,8,7,2]
    ,[9,8,-1,4,-1,2,1,5,6],[4,6,5,1,8,9,2,3,7],[1,2,-1,5,-1,6,4,8,9],
    [8,9,2,7,4,3,5,6,1],[6,3,4,9,5,1,7,2,8],[7,5,1,2,6,8,3,9,4]]

    print(solve_sudoku(example_board))
    print(example_board)
