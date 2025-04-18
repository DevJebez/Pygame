"""
This file defines the object paddle
"""

import pygame

from settings import SCREEN_WIDTH, PADDLE_COLOR



class Paddle:
    def __init__(self):
        self.width = 100 
        self.height = 20
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = 550
        self.speed = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def move(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)