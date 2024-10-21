import pygame 
from const import *
class Game:
    def __init__(self):
        pass 
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLUMNS):
                if (row+col) %2 == 0:
                    color = (234,238,200) #light green
                else:
                    color = (119,154, 88) # dark green 
                rect = (col*SQSIZE,row * SQSIZE,SQSIZE,SQSIZE)
                #initially col =0 and row = 0
                # 1st argumet  = x position
                # 2nd argument = y position
                # 3rd argument = width of the rectangle
                # 4th argument = height of the rectangle 
                pygame.draw.rect(surface,color,rect)

                
