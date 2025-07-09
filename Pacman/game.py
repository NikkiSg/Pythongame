import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.player = Player(50, 50)
        self.enemy = Enemy(200, 200)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move("left")
            if keys[pygame.K_RIGHT]:
                self.player.move("right")
            if keys[pygame.K_UP]:
                self.player.move("up")
            if keys[pygame.K_DOWN]:
                self.player.move("down")

            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()