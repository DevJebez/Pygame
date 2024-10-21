import pygame
import random
from pygame import mixer
import math

# initializing the pygame
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('sapcebackground.jpg')

# background music
mixer.music.load('melodyloops-freemium-epic-motivation-2m30s.mp3')
mixer.music.play(-1)

# Title / caption and Icon
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load('shuttle.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('space-invaders (1).png')
playerx = 360
playery = 490
playerx_change = 0

# enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 100))
    enemyx_change.append(0.7)
    enemyy_change.append(10)

# bullet

# ready - you can't see the bullet on the screen
# Fire  - the bullet is currently moving
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0.3
bullety_change = 2
bullet_state = 'ready'

# score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',20 )

textX = 10
textY = 10

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 70)

def show_score(x, y):
    score = over_font.render('SCORE :' + str(score_value), True, (255, 0, 0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render('GAME OVER' , True, (255, 0, 0)) 
    screen.blit(over_text ,(200, 250))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if distance < 27:
        return True
    else:
        return False



# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 120, 150))

    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.8
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('GunShotSnglShotEx PE1097508.mp3')
                    bullet_sound.play()
                    # get the current x co-ordinate     of sapceship
                    bulletx = playerx
                    fire_bullet(playerx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    # checking for boundaries so that it doesn't go out of bound
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736

    # enemy movement
    for i in range(num_of_enemies):

        #game over 
        if enemyy[i] > 440 :
            for j in range(num_of_enemies):
                enemyy[j]=100
            game_over_text()
            break


        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.5
            enemyy[i] += enemyy_change[i]
        if enemyx[i] >= 736:
            enemyx_change[i] = -0.5
            enemyy[i] += enemyy_change[i]

        # collision
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = 'ready'
            score_value += 1
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(0, 100)

        enemy(enemyx[i], enemyy[i], i)


    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change



    player(playerx, playery)
    show_score(textX, textY)
    pygame.display.update()
