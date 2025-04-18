# src/brick.py

import pygame
from settings import BRICK_COLOR

class Brick:
    def __init__(self, x, y, width=60, height=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BRICK_COLOR
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, BRICK_COLOR, self.rect, 2)  # border
