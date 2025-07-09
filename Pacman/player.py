import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 255, 0)

    def move(self, direction):
        if direction == "left":
            self.x -= 5
        elif direction == "right":
            self.x += 5
        elif direction == "up":
            self.y -= 5
        elif direction == "down":
            self.y += 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
