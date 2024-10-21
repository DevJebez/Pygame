from const import *

class Board:
    def __init__(self):
        self.squares = [] 
    def _create(self): # _ before method names to represent it as private 
        self.squares = [[0,0,0,0,0,0,0,0] for cols in range(COLUMNS)]
        print(self.squares)
    def _add_pieces(self,color):
        pass 
b= Board()
b._create()