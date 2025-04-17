import pygame
pygame.init()
from pygame import mixer
FPS = 60
# setting height and width of the screen
HEIGHT, WIDTH = 680, 680

mixer.music.load("song.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)
hit_sound = pygame.mixer.Sound("pong.ogg")


# setting the windows display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# paddle's height and width
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
color = (28, 1, 22)
WHITE = (255, 255, 255)
BALL = (255, 255, 0)

# velocity of the paddle
PADDLE_VEL = 10

# velocity of the ball 
BALL_VEL_X = 5
BALL_VEL_Y = 5

pygame.display.set_caption("PING PONG")

# Font for score display
SCORE_FONT = pygame.font.SysFont("comicsans", 40)

def draw_window(p1, p2, ball_position, score):
    WIN.fill(color)
    
    # Draw score
    player1_score = SCORE_FONT.render(f"{score['player1']}", 1, WHITE)
    player2_score = SCORE_FONT.render(f"{score['player2']}", 1, WHITE)
    WIN.blit(player1_score, (WIDTH // 4 - player1_score.get_width() // 2, 20))
    WIN.blit(player2_score, (WIDTH * 3 // 4 - player2_score.get_width() // 2, 20))
    
    # Draw center line
    pygame.draw.line(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    
    # left paddle
    pygame.draw.rect(WIN, GREEN, p1)
    # right paddle 
    pygame.draw.rect(WIN, RED, p2)   
    # creating the ball
    pygame.draw.circle(WIN, BALL, (int(ball_position.x), int(ball_position.y)), 10)

def update_score(ball_position, score):
    """Updates the score if the ball moves past the paddles."""
    if ball_position.x < 0:  # Ball passed player 1 (left side)
        score["player2"] += 1
        return True  # Indicate that the ball needs to be reset

    if ball_position.x > WIDTH:  # Ball passed player 2 (right side)
        score["player1"] += 1
        return True  # Indicate that the ball needs to be reset

    return False  # No score update needed

def ball_movement(ball_position, player1, player2):
    """Handles ball movement and collision with paddles."""
    global BALL_VEL_X, BALL_VEL_Y

    ball_position.x += BALL_VEL_X
    ball_position.y += BALL_VEL_Y

    # Collision with Top & Bottom Walls
    if ball_position.y <= 10 or ball_position.y >= HEIGHT - 10:
        BALL_VEL_Y *= -1

    # Collision with Left Paddle (Player 1)
    if (ball_position.x - 10 <= player1.x + PADDLE_WIDTH and 
        ball_position.x >= player1.x and
        player1.y - 10 <= ball_position.y <= player1.y + PADDLE_HEIGHT + 10):
        hit_sound.play()
        if BALL_VEL_X < 0:  # Only bounce if moving toward the paddle
            BALL_VEL_X *= -1
        
        
    # Collision with Right Paddle (Player 2)
    if (ball_position.x + 10 >= player2.x and
        ball_position.x <= player2.x + PADDLE_WIDTH and
        player2.y - 10 <= ball_position.y <= player2.y + PADDLE_HEIGHT + 10):
        hit_sound.play()
        if BALL_VEL_X > 0:  # Only bounce if moving toward the paddle
            BALL_VEL_X *= -1
            
def player2_movement(keys_pressed, player):
    # checking upper bound -- up
    if keys_pressed[pygame.K_KP_8] and player.y - PADDLE_VEL > 0:
        player.y -= PADDLE_VEL 
    # checking lower bound -- down
    if keys_pressed[pygame.K_KP_2] and player.y + PADDLE_VEL + PADDLE_HEIGHT <= HEIGHT:
        player.y += PADDLE_VEL

def player1_movement(keys_pressed, player):
    # checking upper bound -- up
    if keys_pressed[pygame.K_w] and player.y - PADDLE_VEL > 0:
        player.y -= PADDLE_VEL 
    # checking lower bound -- down
    if keys_pressed[pygame.K_s] and player.y + PADDLE_VEL + PADDLE_HEIGHT <= HEIGHT:
        player.y += PADDLE_VEL

def main():
    global BALL_VEL_X, BALL_VEL_Y
    player1 = pygame.Rect(20, HEIGHT // 2 - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
    player2 = pygame.Rect(WIDTH - PADDLE_WIDTH - 20, HEIGHT // 2 - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_position = pygame.Vector2(WIDTH // 2, HEIGHT // 2)

    score = {"player1": 0, "player2": 0}  # Store scores

    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return

        keys_pressed = pygame.key.get_pressed()
        player1_movement(keys_pressed, player1)
        player2_movement(keys_pressed, player2)

        ball_movement(ball_position, player1, player2)

        if update_score(ball_position, score):  # Check if a player scored
            ball_position.x, ball_position.y = WIDTH // 2, HEIGHT // 2  # Reset ball
            BALL_VEL_X = abs(BALL_VEL_X) if ball_position.x < 0 else -abs(BALL_VEL_X)  # Serve toward the player who lost
            BALL_VEL_Y = 5 * (1 if pygame.time.get_ticks() % 2 == 0 else -1)  # Random up/down direction

        draw_window(player1, player2, ball_position, score)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()