import numpy as np

class Game:

    def __init__(self):
        self.mat = None
        self.row = 0
        self.col = 0
        self.turn = 0
        self.wins = 0

    #Creates game board based on
    def createBoard(self):
        self.mat = np.zeros((self.row, self.col))


myGame = Game()
myGame.row = 5
myGame.col = 6

myGame.createBoard()

print (myGame.mat)
