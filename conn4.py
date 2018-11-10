import numpy as np
import random
from copy import deepcopy

class Game:
    mat = None
    rows = 0
    cols = 0
    turn = 0
    wins = 0

def check_victory(game):
    board = game.mat
    #check | victory
    for y in range(game.cols):
        for x in range(game.rows - (game.wins-1)):
            if board[x][y] != 0:
                piece = board[x][y]
                count = 0
                for z in range(game.wins):
                    if board[x+z][y] == piece:
                        count += 1
                if count == game.wins:
                    return piece
    
    #check - victory
    for x in range(game.rows):
        for y in range(game.cols - (game.wins-1)):
            if board[x][y] != 0:
                piece = board[x][y]
                count = 0
                for z in range(game.wins):
                    if board[x][y+z] == piece:
                        count += 1
                if count == game.wins:
                    return piece
    
    #check / victory
    for x in range(game.rows - (game.wins-1)):
        for y in range((game.wins-1), game.cols):
            if board[x][y] != 0:
                piece = board[x][y]
                count = 0
                for z in range(game.wins):
                    if board[x+z][y-z] == piece:
                        count += 1
                if count == game.wins:
                    return piece
    #check \ victory
    for x in range(game.rows - (game.wins-1)):
        for y in range(game.cols - (game.wins-1)):
            if board[x][y] != 0:
                piece = board[x][y]
                count = 0
                for z in range(game.wins):
                    if board[x+z][y+z] == piece:
                        count += 1
                if count == game.wins:
                    return piece

    if is_full(game):
        #Board is full therefore draw
        return 3
    
    #If code managed to reach here, means neither player has won or it is not a draw
    #Therefore there is no conclusive victory
    return 0

def apply_move(game, col, pop):
    if pop == False:
        for x in range(game.rows):
            if game.mat[x][col] == 0:
                game.mat[x][col] = game.turn
                break
    else:
        for x in range(game.rows - 1):
            game.mat[x][col] = game.mat[x + 1][col]

        game.mat[game.rows-1][col] = 0
    
    if game.turn == 1:
        game.turn = 2
    else:
        game.turn = 1

    return game

def check_move(game, col, pop):
    if pop == False:
        if game.mat[game.rows-1][col] == 0:
            return True
    else:
        if game.mat[0][col] != 0:
            return True

    return False

def random_move(game):
    while True:
        col = random.randint(0,game.cols-1)
        pop = random.randint(1,2)
        
        if pop == 1:
            p = False
        elif pop ==2:
            p = True
        
        if check_move(game, col, p):
            apply_move(game, col, p)
            return (col, p)
                
def computer_move(game, level):
    if level == 1:
        return random_move(game)
    elif level == 2:

        for y in range(game.cols):
            tempGame = deepcopy(game)
            tempGame.turn = 2

            if check_move(tempGame, y, False):
                apply_move(tempGame, y, False)

                if check_victory(tempGame) == 2:
                    apply_move(game, y, False)
                    return(y, False)

        for y in range(game.cols):
            tempGame = deepcopy(game)
            tempGame.turn = 2

            if check_move(tempGame, y, True):
                apply_move(tempGame, y, True)

                if check_victory(tempGame) == 2:
                    apply_move(game, y, True)
                    return (y, True)

        for y in range(game.cols):
            tempGame = deepcopy(game)
            tempGame.turn = 1

            if check_move(tempGame, y, False):
                apply_move(tempGame, y, False)

                if check_victory(tempGame) == 1:
                    apply_move(game, y, False)
                    return(y, False)

        return random_move(game)

def display_board(game):
    print("\n*********Game Board*********\n")
    for x in range(game.rows):
        for y in range(game.cols):
            print(str(int(game.mat[game.rows -1 -x][y])) + "\t"),
        print ("\n")
    #print(game.mat)

def is_full(game):
    for x in range(game.rows):
        for y in range(game.cols):
            if game.mat[x][y] == 0:
                return False
    return True

def menu():
    game = Game()
    print ("Welcome to Connect Four!\n\nPlease enter the number of rows and columns for your board")
    rows = input("Rows: ")
    cols = input("Cols: ")

    wins = -1
    
    while wins < 0:
        wins = input("Please enter the number of pieces to win: ")
        
        if wins > min(rows, cols):
            wins = -1
            print("Please enter a value that is less than " + str(min(rows, cols)))
    

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

    game.rows = rows
    game.cols = cols
    game.wins = wins
    game.turn = 1
    game.mat = np.zeros((game.rows,game.cols))
    display_board(game)

    while check_victory(game) == 0:
        c = -1
        p = -1
        validHumanMove = False

        print ("\n**Player " + str(game.turn) + "'s turn**")

        while c == -1:
            tmp = input("Enter a column to insert/pop: ")

            if tmp >= 0 and tmp < game.cols:
                c = tmp
            else:
                print("Please enter a valid column!")


        while not (p == 1 or p == 2):
            print("Do you wish to: \n 1. Insert\n 2. Pop\n")
            p = input("Choice: ")

            if not (p == 1 or p == 2):
                print ("Please enter a valid choice!")
            
            if p == 1:
                pop = False
            elif p == 2:
                pop = True

        if check_move(game, c, pop):
            validHumanMove = True
            apply_move(game, c, pop)
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

        if (com == 2 and validHumanMove):
            print ("\n**Player " + str(game.turn) + "'s turn**")
            moveCol, movePop = computer_move(game, diff)
            display_board(game)

            if movePop:
                print("Computer has popped column " + str(moveCol) + "!!!")
            else:
                print("Computer has inserted on column " + str(moveCol) + "!!!")

            if check_victory(game) == 1:
                print("Player 1 has won!")
                break
            elif check_victory(game) == 2:
                print("Player 2 has won!")
                break
            elif check_victory(game) == 3:
                print("The game is a draw!")
                break

menu()