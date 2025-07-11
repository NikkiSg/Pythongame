import pygame
import random
import math

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.color = (255, 0, 0)
        self.speed = 3

    def distance_to_player(self, player):
        return math.hypot(player.x - self.x, player.y - self.y)

    def move_towards_player(self, player):
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.hypot(dx, dy)

        if distance == 0:
            return

        self.x += self.speed * (dx / distance)
        self.y += self.speed * (dy / distance)

    def move_random(self):
        direction = random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        elif direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed

    def update(self, player):
        if self.distance_to_player(player) < 100:
            self.move_towards_player(player)
        else:
            self.move_random()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))
