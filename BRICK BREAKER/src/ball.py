# src/ball.py

import pygame
from settings import BALL_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Ball:
    def __init__(self):
        self.radius = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = 5
        self.dy = -5

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Wall collisions
        if self.x - self.radius <= 0 or self.x + self.radius >= SCREEN_WIDTH:
            self.dx *= -1
        if self.y - self.radius <= 0:
            self.dy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, BALL_COLOR, (self.x, self.y), self.radius)

    def collide_with_paddle(self, paddle_rect):
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)
        if ball_rect.colliderect(paddle_rect):
            self.dy *= -1
