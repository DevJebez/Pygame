import pygame 
import sys
import os 
from const import * #imports everything from const file 

from game import Game 



class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
        pygame.display.set_caption("CHESSIEEEE")  
        self.game = Game()
    def mainloop(self):
        game = self.game 
        screen = self.screen 
        run = True
        while run:
            game.show_bg(screen)
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
  
main = Main() #creating an instance of a class 
main.mainloop()