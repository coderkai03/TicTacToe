'''
1. player profiles
2. board setup
3. turn mechanics
4. win mechanics
'''

from profiles import Player
from gamelogic import TicTacToe
import random

def main():
    print('=> Tic Tac Toe! <=')

    #create game
    game = TicTacToe()

    #user input
    xInput = 0
    yInput = 0

    #rand turn gen
    turn = random.randint(1, 2)
    turn = -1 if turn == 1 else 1

    #get player names
    name1 = input('< Player 1 >\nName: ')
    age1 = input('Age: ')
    print()
    name2 = input('< Player 2 >\nName: ')
    age2 = input('Age: ')
    print()

    #create players
    p1 = Player(name1, age1)
    p2 = Player(name2, age2)

    print('-------------------\n')

    while not (xInput == yInput == -1):
        currPlayer = p1.getName() if turn == -1 else p2.getName()
        game.displayBoard()
        print(f'{currPlayer}\'s turn')

        #ask user for move
        xInput = int(input('Enter [x] coord: '))-1
        yInput = int(input('Enter [y] coord: '))-1

        #process move
        if xInput != -1 and yInput != -1:
            game.placeMove(yInput, xInput, turn)
            
        print('-------------------\n')
        
        #check if player wins
        if game.checkWin(yInput, xInput, turn) == True:
            print(f'{currPlayer} won!')
            break

        #switch turns
        turn *= -1
        

    game.displayBoard()

main()