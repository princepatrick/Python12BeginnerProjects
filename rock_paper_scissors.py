import random

def play():
    user = input("Enter your choice - [\'R\' for Rock, \'S\' for Scissors, \'P\' for Paper]: ")
    computer = random.choice(['R', 'P', 'S'])
    
    if user == computer:
        print('It\'s a tie')
        return
    
    if computeWinner(user, computer):
        print('You won!!!')
        return
    
    print("You lost...")

def computeWinner(u, c):
    # R > S, P > R, S > P
    if (u=='R' and c=='S') or (u=='P' and c=='R') or (u=='S' and c=='P') :
        return True

play()