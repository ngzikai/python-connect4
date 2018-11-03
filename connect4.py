
import numpy as np

class Game:
    def __init__(self, rows, cols):
        self.mat = np.zeros((rows, cols))
        self.row = rows
        self.col = cols
        self.turn = 0
        self.wins = 0

def check_victory(game):
    board = game.mat

    # check horizontal spaces for human player
    for y in range(game.row):
        for x in range(game.col - 3):
            if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                return 1

    # check vertical spaces for human player
    for x in range(game.col):
        for y in range(game.row - 3):
            if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
                return 1

    # check / diagonal spaces for human player
    for x in range(game.col - 3):
        for y in range(3, game.row):
            if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                return 1

    # check \ diagonal spaces for human player
    for x in range(game.col - 3):
        for y in range(game.row - 3):
            if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                return 1

    # check horizontal spaces for computer player
    for y in range(game.row):
        for x in range(game.col - 3):
            if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                return 2

    # check vertical spaces for computer player
    for x in range(game.col):
        for y in range(game.row - 3):
            if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
                return 2

    # check / diagonal spaces for computer player
    for x in range(game.col - 3):
        for y in range(3, game.row):
            if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                return 2

    # check \ diagonal spaces for computer player
    for x in range(game.col - 3):
        for y in range(game.row - 3):
            if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                return 2

    #board is full and neither computer nor hunans are winning
    if is_full(game):
        return 3

    return 0

def apply_move(game, col, pop):
    for x in range(game.row):
        if game.mat[game.row - x-1][col] == 0:
            game.mat[game.row - x-1][col] = pop
            break

def check_move(game, col, pop):
    pass

def computer_move(game, level):
    pass

def display_board(game):
    print(game.mat)

def is_full(game):
    for x in range(game.row):
        for y in range(game.col):
            if game.mat[x][y] == 0:
                return False
    return True

def menu():
    print ("Welcome to Connect Four! Please enter the number of rows and columns for your board")
    r = input("Rows: ")
    c = input("Cols: ")

    game = Game(r, c)

    # game.mat[1][3] = 1
    # game.mat[0][0] = 2
    # game.mat[4][5] = 3

    apply_move(game, 0, 1)
    apply_move(game, 1, 2)
    apply_move(game, 1, 1)
    apply_move(game, 2, 2)
    apply_move(game, 2, 2)
    apply_move(game, 2, 1)
    apply_move(game, 3, 2)
    apply_move(game, 3, 2)
    apply_move(game, 3, 2)
    apply_move(game, 3, 1)


    display_board(game)

    if check_victory(game) == 1:
        print("Human has won!")

    print(is_full(game))

if __name__ == "__main__":
    menu()

#
# def isWinner(board, tile):
#     # check horizontal spaces
#     for y in range(BOARDHEIGHT):
#         for x in range(BOARDWIDTH - 3):
#             if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
#                 return True
#
#     # check vertical spaces
#     for x in range(BOARDWIDTH):
#         for y in range(BOARDHEIGHT - 3):
#             if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
#                 return True
#
#     # check / diagonal spaces
#     for x in range(BOARDWIDTH - 3):
#         for y in range(3, BOARDHEIGHT):
#             if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
#                 return True
#
#     # check \ diagonal spaces
#     for x in range(BOARDWIDTH - 3):
#         for y in range(BOARDHEIGHT - 3):
#             if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
#                 return True
#
#     return False
