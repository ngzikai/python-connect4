
import numpy as np
import random
from copy import deepcopy

class Game:
    def __init__(self, rows, cols):
        self.mat = np.zeros((rows, cols))
        self.row = rows
        self.col = cols
        self.turn = 1
        self.wins = 0

def check_victory(game):
    board = game.mat

    for y in range(game.col):
        for x in range(game.row - 3):
            if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                return 1

    for x in range(game.row):
        for y in range(game.col - 3):
            if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
                return 1

    for x in range(game.row - 3):
        for y in range(3, game.col):
            if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                return 1

    for x in range(game.row - 3):
        for y in range(game.col - 3):
            if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                return 1

    for y in range(game.col):
        for x in range(game.row - 3):
            if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                return 2

    for x in range(game.row):
        for y in range(game.col - 3):
            if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
                return 2

    for x in range(game.row - 3):
        for y in range(3, game.col):
            if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                return 2

    for x in range(game.row - 3):
        for y in range(game.col - 3):
            if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                return 2

    if is_full(game):
        return 3

    return 0

def apply_move(game, col, pop):
    if pop == 1:
        for x in range(game.row):
            if game.mat[game.row - x-1][col] == 0:
                game.mat[game.row - x-1][col] = game.turn
                break
    else:
        for x in range(game.row - 1):
            game.mat[game.row - x -1][col] = game.mat[game.row - x - 2][col]

        game.mat[0][col] = 0

def check_move(game, col, pop):
    if pop == 1:
        if game.mat[0][col] == 0:
            return True
    else:
        if game.mat[game.row-1][col] != 0:
            return True

    return False

def computer_move(game, level):
    if level == 1:
        while True:
            col = random.randint(0,game.col-1)
            pop = random.randint(1,2)

            if check_move(game, col, pop):
                apply_move(game, col, pop)
                break

    elif level == 2:
        moveApplied = 0

        while moveApplied == 0:
            for y in range(game.col):
                tempGame = deepcopy(game)
                tempGame.turn = 2

                if check_move(tempGame, y, 1):
                    apply_move(tempGame, y, 1)

                    if check_victory(tempGame) == 2:
                        apply_move(game, y, 1)
                        moveApplied = 1
                        break


            for y in range(game.col):
                tempGame = deepcopy(game)
                tempGame.turn = 2

                if check_move(tempGame, y, 2):
                    apply_move(tempGame, y, 2)

                    if check_victory(tempGame) == 2:
                        apply_move(game, y, 2)
                        moveApplied = 1
                        break

            for y in range(game.col):
                tempGame = deepcopy(game)
                tempGame.turn = 1

                if check_move(tempGame, y, 1):
                    apply_move(tempGame, y, 1)

                    if check_victory(tempGame) == 1:
                        apply_move(game, y, 1)
                        moveApplied = 1
                        break

            if moveApplied == 0:
                #print("Entered loop")
                while True:
                    col = random.randint(0,game.col-1)
                    pop = random.randint(1,2)

                    if check_move(game, col, pop):
                        apply_move(game, col, pop)
                        moveApplied = 1
                        break

def display_board(game):
    print("\n*********Game Board*********\n")
    s = [[str(int(i)) for i in row] for row in game.mat]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def is_full(game):
    for x in range(game.row):
        for y in range(game.col):
            if game.mat[x][y] == 0:
                return False
    return True

def menu():
    print ("Welcome to Connect Four!\n\nPlease enter the number of rows and columns for your board")
    r = input("Rows: ")
    c = input("Cols: ")

    com = -1
    while not (com == 1 or com == 2):
        print("\nPlease select your game mode:\n1. Human vs. Human\n2. Human vs. Computer\n")
        com = input("Choice: ")

        if not (com == 1 or com == 2):
            print ("Please enter a valid choice!")

    if com == 2:
        diff = -1
        while not (diff == 1 or diff == 2):
            print("\nPlease select your difficulty:\n1. Easy\n2. Medium\n")
            diff = input("Choice: ")

            if not (diff == 1 or diff == 2):
                print ("Please enter a valid choice!")

    game = Game(r, c)
    display_board(game)

    while check_victory(game) == 0:
        c = -1
        p = -1

        print ("\n**Player " + str(game.turn) + "'s turn**")

        while c == -1:
            tmp = input("Enter a column to insert/pop: ")

            if tmp >= 0 and tmp < game.col:
                c = tmp
            else:
                print("Please enter a valid column!")


        while not (p == 1 or p == 2):
            print("Do you wish to: \n 1. Insert\n 2. Pop\n")
            p = input("Choice: ")

            if not (p == 1 or p == 2):
                print ("Please enter a valid choice!")

        if check_move(game, c, p):
            apply_move(game, c, p)
            if game.turn == 1:
                game.turn = 2
            else:
                game.turn = 1
            display_board(game)

            if check_victory(game) == 1:
                print("Player 1 has won!")
                break
            elif check_victory(game) == 2:
                print("Player 2 has won!")
                break
            elif check_victory(game) == 3:
                print("The game is a draw!")
                break
        else:
            print ("The move is not valid, please enter again")

        if com == 2:
            print ("\n**Player " + str(game.turn) + "'s turn**")
            computer_move(game, diff)
            if game.turn == 1:
                game.turn = 2
            else:
                game.turn = 1
            display_board(game)

            if check_victory(game) == 1:
                print("Player 1 has won!")
                break
            elif check_victory(game) == 2:
                print("Player 2 has won!")
                break
            elif check_victory(game) == 3:
                print("The game is a draw!")
                break

if __name__ == "__main__":
    menu()
