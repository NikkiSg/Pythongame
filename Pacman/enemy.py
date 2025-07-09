import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
