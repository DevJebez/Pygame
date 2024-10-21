import pygame,os
pygame.font.init() #intialzing the font lib here
pygame.mixer.init()
HEIGHT, WIDTH = 1200,680    
WIN = pygame.display.set_mode((HEIGHT, WIDTH ))
pygame.display.set_caption("FIRST GAME!")
BULLET_VELOCITY = 7
BORDER = pygame.Rect(HEIGHT/2-5,0,10,WIDTH) 
# it takes 4 parameters, first two are positions 
#where the rectangle should be drawn
#the next two are the width and height of the rectangle
color=(28,1,22)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

FPS = 120 
VEL = 5
MAX_BULLETS =4
HEALTH_FONT = pygame.font.SysFont('comicsans',40)
PLAYER_1 = pygame.image.load(os.path.join('E:\JEBEZ\WORKING WITH PYTHON\LEARNING PYGAME\SPACE INVADERS 1V1\player1.png'))
# To Transform the size of the image  and rotate
#PLAYER1=pygame.transform.rotate(pygame.transform.scale(PLAYER_1,(100,100)),90) #this rotates to 90 to anticlockwise
WINNER_FONT = pygame.font.SysFont('comicsans',100)

PLAYER_2 = pygame.image.load(os.path.join('E:\JEBEZ\WORKING WITH PYTHON\LEARNING PYGAME\SPACE INVADERS 1V1\player2.png'))
#To transform the size of the image
#PLAYER2 = pygame.transform.rotate(pygame.transform.scale(PLAYER_2(100,100)),270    )

#loading background
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('E:/JEBEZ/WORKING WITH PYTHON/LEARNING PYGAME/SPACE INVADERS 1V1/bg.png')),(HEIGHT,WIDTH))

PLAYER1_HIT = pygame.USEREVENT+1 #CREATING AN EVENT as 1 [this can be a random number]
PLAYER2_HIT = pygame.USEREVENT+2    

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(r'E:\JEBEZ\WORKING WITH PYTHON\LEARNING PYGAME\SPACE INVADERS 1V1\laser.wav'))
pygame.mixer.music.load(r'E:\JEBEZ\WORKING WITH PYTHON\LEARNING PYGAME\SPACE INVADERS 1V1/background.wav')
pygame.mixer.music.play(-1)




def draw_window(p1, p2, p1_bullets, p2_bullets,p1_health,p2_health):
    WIN.fill(color)
    #WIN.blit(SPACE,(0,0 ))
    pygame.draw.rect(WIN,GREEN,BORDER)
    p1_health_text = HEALTH_FONT.render("Health :"+str(p1_health),1,(255,255,255)) #1 - Antialias, color
    p2_health_text = HEALTH_FONT.render("Health :"+str(p2_health),1,(255,255,255))
    WIN.blit(p1_health_text,(HEIGHT - p1_health_text.get_width()-10,10))
    WIN.blit(p2_health_text,(10,10))
    WIN.blit(PLAYER_1,(p1.x,p1.y))
    WIN.blit(PLAYER_2,(p2.x,p2.y))
    for bullet in p1_bullets:
        pygame.draw.rect(WIN, RED, bullet)
             
    for bullet in p2_bullets:
        pygame.draw.rect(WIN, YELLOW,bullet)
    pygame.display.update()



def player1_movement(keys_pressed,player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0:#LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL + player.width < BORDER.x:#RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w] and player.y - VEL > 0:#UP
        player.y -= VEL
    if keys_pressed[pygame.K_s] and player.y + VEL + player.height < WIDTH :#DOWN   
        player.y += VEL
def player2_movement(keys_pressed,player):
    if keys_pressed[pygame.K_j] and player.x - VEL > BORDER.x+10:#LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_l] and player.x + VEL + player.width < HEIGHT:#RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_i] and player.y - VEL > 0:#UP
        player.y -= VEL
    if keys_pressed[pygame.K_k] and player.y + VEL + player.height < WIDTH:#DOWN   
        player.y += VEL

def handle_bullets(p1_bullets,p2_bullets,player1,player2):
    for bullets in p1_bullets:
        bullets.x += BULLET_VELOCITY
        #CHECKING player1 bullet hitting player2
        if player2.colliderect(bullets):# this works if the both are rectangles 
            pygame.event.post(pygame.event.Event(PLAYER1_HIT))
            p1_bullets.remove(bullets)
        elif bullets.x > HEIGHT :
            p1_bullets.remove(bullets)
    for bullets in p2_bullets:
        bullets.x -= BULLET_VELOCITY
        #CHECKING player2 bullet hitting player1
        if player1.colliderect(bullets):# this works if the both are rectangles 
            pygame.event.post(pygame.event.Event(PLAYER2_HIT))
            p2_bullets.remove(bullets)
        elif bullets.x <0:
            p2_bullets.remove(bullets)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1,(255,255,255))
    WIN.blit(draw_text ,(WIDTH/2 - draw_text.get_height()/2,HEIGHT/2- draw_text.get_width()/2))
    pygame.display.update()
    pygame.time.delay(5000)



def main():
    player1 = pygame.Rect(100,300,64,64)
    player2 = pygame.Rect(1050,300,64,64)
    clock = pygame.time.Clock()
    p1_bullets =[]
    p2_bullets = []
    p1_health = 10
    p2_health = 10
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #this gets all the events that happens in that window
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(p1_bullets) < MAX_BULLETS:
                    #defining the position of the bullet
                    # 1st argument = x position """ 
                    #we adding width to it to make it look like from front" in 1st argument
                    #2nd argument = y position
                    #3rd and 4th size of the bullet - rectangle 
                    bullet = pygame.Rect(player1.x + player1.width,player1.y+player1.height//2-2,20,10)
                    p1_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_SPACE and len(p2_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player2.x,player2.y+player2.height//2-2,20,10)
                    p2_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == PLAYER1_HIT:
                p1_health -=1
            if event.type == PLAYER2_HIT:
                p2_health -=1
        winner_text = ''
        if p1_health <=0:
            winner_text = 'Player 2 Wins'
        if p2_health <=0:
            winner_text = 'Player 1 Wins'
        if winner_text!='':
            draw_winner(winner_text)
            break

        
        
        
        keys_pressed = pygame.key.get_pressed() #stores the key that pressed runs 60 times per sec
        player1_movement(keys_pressed,player1)
        player2_movement(keys_pressed,player2)
        #handling bullts
        handle_bullets(p1_bullets,p2_bullets,player1,player2)
        draw_window(player1,player2,p1_bullets,p2_bullets,p1_health,p2_health)

    main()
if __name__ == "__main__":
    main()