import pygame,os 
pygame.font.init()
pygame.mixer.init()
FPS = 60
# setting height and width of the screen
HEIGHT, WIDTH = 680,680

#setting the windows display
WIN = pygame.display.set_mode((HEIGHT,WIDTH))

#paddle's height and width
PADDLE_WIDTH, PADDLE_HEIGHT = 20,100

#drawing border for collision 

#BORDER = pygame.Rect(HEIGHT/2-5,0,10,WIDTH) 
clock = pygame.time.Clock()
'''

Player's paddle dimension 
width, height = 20,100    


player1 coordinates = 300,50,100,20
player2 coordinates  = 300,590,100,20'


player 1 coordinates new 
x axis = 20
y axis = HEIGHT//2 - (PADDLE_HEIGHT//2)

player 2 coordinates new 
x axis = WIDTH - 10
y axis = HEIGHT//2 - (PADDLE_HEIGHT//2)

'''
GREEN = (0,255,0)
RED = (255,0,0)
color=(28,1,22) 
WHITE = (255,255,255)
BALL = (255,255,0)

#velocity of the paddle
PADDLE_VEL = 1

#velocity of the ball 
BALL_VEL_X= 10
BALL_VEL_Y = 1
pygame.display.set_caption("PING PONG")


def draw_window(p1,p2,ball_position):

    WIN.fill(color)
    # left paddle
    pygame.draw.rect(WIN,GREEN,p1)
    # right paddle 
    pygame.draw.rect(WIN,RED,p2)   
    #creating the ball
    pygame.draw.circle(WIN,BALL,ball_position,10)

def ball_movement(keys_pressed,ball_position):
    if keys_pressed[pygame.K_SPACE]:
        ball_position.x += BALL_VEL_X
    #ball_position.y += BALL_VEL_Y


def player2_movement(keys_pressed,player):
    # movement for upward
    # checking upper bound -- up
    if keys_pressed[pygame.K_KP8] and player.y - PADDLE_VEL > 0:
        player.y -= PADDLE_VEL 
    #checking lower bound -- down
    if keys_pressed[pygame.K_KP2] and player.y + PADDLE_VEL <= HEIGHT - PADDLE_HEIGHT:
        print(f"player2_y:{player.y}")
        player.y += PADDLE_VEL


def player1_movement(keys_pressed,player):
    # movement for upward
    # checking upper bound -- up
    if keys_pressed[pygame.K_w] and player.y - PADDLE_VEL > 0:
        player.y -= PADDLE_VEL 
    #checking lower bound -- down
    if keys_pressed[pygame.K_s] and player.y + PADDLE_VEL  < HEIGHT-PADDLE_HEIGHT:
        player.y += PADDLE_VEL

def main():
    player1 = pygame.Rect(20,HEIGHT//2 - (PADDLE_HEIGHT//2),PADDLE_WIDTH,PADDLE_HEIGHT)
    player2 = pygame.Rect(WIDTH - PADDLE_WIDTH - 20,HEIGHT//2 - (PADDLE_HEIGHT//2),PADDLE_WIDTH,PADDLE_HEIGHT)
    print(player1)
    print(player2)
    run = True
    p1_health = 0
    p2_health = 0
    clock.tick(FPS)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit() 

        keys_pressed = pygame.key.get_pressed() #stores the key that pressed runs 60 times per sec
        player1_movement(keys_pressed,player1)
        player2_movement(keys_pressed,player2)

        ball_position = pygame.Vector2(WIN.get_width() / 2, WIN.get_height() / 2)
        ball_movement(keys_pressed,ball_position)
        draw_window(player1,player2,ball_position)

        # to display the work on the screen
        pygame.display.flip()
    main()

if __name__ == "__main__":
    main()