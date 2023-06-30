class TicTacToe:
    def __init__(s):
        #create a 3x3 board with *'s
        s.board = [['□' for i in range(3)] for j in range(3)]

    def displayBoard(s):
        #display the board
        for row in s.board:
            for col in row:
                print(col, ' ', end='')
            print('\n')
            
    def placeMove(s, x, y, turn):
        if s.board[x][y] == '□' and 0 <= x <= 2 and 0 <= y <= 2:
            s.board[x][y] = 'X' if turn == -1 else 'O'

    def checkWin(s, x, y, turn):
        token = ('X' if turn == -1 else 'O')*3

        #horiz diagnoal
        validHoriz = True if ''.join(s.board[x]) == token else False

        #vert diagonal
        validVert = True if (s.board[0][y]+s.board[1][y]+s.board[2][y]) == token else False

        #TL->BR diagonal
        TLBR = True if (s.board[0][0]+s.board[1][1]+s.board[2][2]) == token else False

        #BL->TR diagonal
        BLTR = True if (s.board[0][2]+s.board[1][1]+s.board[2][0]) == token else False

        return True if validVert or validHoriz or TLBR or BLTR else False