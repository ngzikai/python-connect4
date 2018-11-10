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
    #Check | victory
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
    
    #Check - victory
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
    
    #Check / victory
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
    #Check \ victory
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

    # Realise that the board is flipped, but doesn't matter

    if is_full(game):
        #Board is full therefore draw
        return 3
    
    #If code managed to reach here, means neither player has won or it is not a draw
    #Therefore there is no conclusive victory
    return 0

def apply_move(game, col, pop):
    if pop == False:
        #Insertion move: Find the first zero value per given column and add the current player's value 
        for x in range(game.rows):
            if game.mat[x][col] == 0:
                game.mat[x][col] = game.turn
                break
    else:
        #Pop move: For the entire column, set the value of the current value to the one one row below it
        for x in range(game.rows - 1):
            game.mat[x][col] = game.mat[x + 1][col]
        #Bottom most value per row should be a 0
        game.mat[game.rows-1][col] = 0
    
    #Swap players player 1 becomes player 2, vice versa
    if game.turn == 1:
        game.turn = 2
    else:
        game.turn = 1

    return game

def check_move(game, col, pop):
    if pop == False:
        #If the last value of the column has is 0 (has empty slots), the column can still be inserted
        if game.mat[game.rows-1][col] == 0:
            return True
    else:
        #If the first slot of the column (which is in fact, the bottom slot most in the game) is not 0, the column can be popped
        if game.mat[0][col] != 0:
            return True

    return False

def random_move(game):
    while True:
        #Select random column and pop value
        col = random.randint(0,game.cols-1)
        pop = random.randint(1,2)
        
        if pop == 1:
            p = False
        elif pop ==2:
            p = True
        #Check if it's a valid move, else just reroll
        if check_move(game, col, p):
            apply_move(game, col, p)
            return (col, p)
                
def computer_move(game, level):
    if level == 1:
        #Perform random move 
        return random_move(game)
    elif level == 2:
        #Check if computer can win if it insert pieces into any column
        for y in range(game.cols):
            #To preserve the integrity of our gameboard, we make a copy as tempGame
            tempGame = deepcopy(game)
            tempGame.turn = 2

            if check_move(tempGame, y, False):
                #If the move is valid for the column, perform insertion on tempGame
                apply_move(tempGame, y, False)

                #If the insertion results in computer winning, then perform it on actual game board
                if check_victory(tempGame) == 2:
                    apply_move(game, y, False)
                    return(y, False)
        
        #Check if the computer can win if it popped any column
        #Detailed logic is roughly the same as above
        for y in range(game.cols):
            tempGame = deepcopy(game)
            tempGame.turn = 2

            if check_move(tempGame, y, True):
                apply_move(tempGame, y, True)

                if check_victory(tempGame) == 2:
                    apply_move(game, y, True)
                    return (y, True)
        
        #Check if the player is will win in the next move, if so, apply the move to prevent player from winning 
        for y in range(game.cols):
            tempGame = deepcopy(game)
            tempGame.turn = 1

            if check_move(tempGame, y, False):
                apply_move(tempGame, y, False)

                if check_victory(tempGame) == 1:
                    apply_move(game, y, False)
                    return(y, False)

        #I am not smart enough to determine how is it possible to prevent the human player from winning through popping :(

        #If there is no smarter move to be made, perform random move
        return random_move(game)

def display_board(game):
    print("\n*********Game Board*********\n")
    #Flip the board on y-axis and print
    for x in range(game.rows):
        for y in range(game.cols):
            print(str(int(game.mat[game.rows -1 -x][y])) + "\t"),
        print ("\n")

def is_full(game):
    #If there are no more 0 values in the matrix, the board must be filled with player values, therefore full
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