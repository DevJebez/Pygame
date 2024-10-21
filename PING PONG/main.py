import pygame,os 
pygame.font.init()
pygame.mixer.init()
FPS = 60
HEIGHT, WIDTH = 680,680
WIN = pygame.display.set_mode((HEIGHT,WIDTH))
clock = pygame.time.Clock()
'''
player1 coordinates = 300,50,100,20
player2 coordinates  = 300,590,100,20'

'''
GREEN = (0,255,0)
RED = (255,0,0)
color=(28,1,22)
pygame.display.set_caption("PING PONG")


def draw_window(p1,p2):
    pygame.draw.rect(WIN,GREEN,p1)
    pygame.draw.rect(WIN,RED,p2)


def main():
    player1 = pygame.Rect(290,50,100,10)
    player2 = pygame.Rect(290,590,100,10)
    run = True
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()   
        draw_window(player1,player2)
        pygame.display.flip()
    main()

if __name__ == "__main__":
    main()