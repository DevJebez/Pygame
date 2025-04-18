"""
This file handles game loop and event handling
"""


import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BLACK
from paddle import Paddle
from ball import Ball
from brick import Brick

def create_bricks(rows, cols, padding = 10, offset_y = 20):
    bricks = []
    brick_width = 60
    brick_height = 20
    total_width = cols * (brick_width + padding) - padding
    start_x = (SCREEN_WIDTH - total_width) // 2

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (brick_width + padding)
            y = offset_y + row * (brick_height + padding)
            bricks.append(Brick(x, y, brick_width, brick_height))
    return bricks
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Brick Breaker")
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks(rows = 5, cols = 10)  # 5 rows and 10 columns of bricks    

    running = True
    while running:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for brick in bricks:
            if brick.alive:
                brick.rect = brick.rect 
                ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius*2, ball.radius*2)  
                if ball_rect.colliderect(brick.rect):
                    brick.alive = False
                    ball.dy *= -1
                    break 
        
        paddle.move(keys)
        ball.move()
        ball.collide_with_paddle(paddle.rect)

        screen.fill(BLACK)
        paddle.draw(screen)
        for brick in bricks:
            brick.draw(screen)
        ball.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
