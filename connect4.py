
import numpy as np

class Game:
    def __init__(self):
        self.mat = None
        self.row = 0
        self.col = 0
        self.turn = 0
        self.wins = 0

    #Creates game board based on rows and cols
    def create_board(self):
        self.mat = np.zeros((self.row, self.col))

def check_victory(game):
    pass

def apply_move(game, col, pop):
    pass

def check_move(game, col, pop):
    pass

def computer_move(game, level):
    pass

def display_board(game):
    print(game.mat)

def menu():
    pass



myGame = Game()
myGame.row = 5
myGame.col = 6

myGame.createBoard()
print (myGame.mat)

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
