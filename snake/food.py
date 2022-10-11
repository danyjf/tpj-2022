import pygame
import random

from environment import Environment

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Environment.SCALE, Environment.SCALE))
        self.rect = self.image.get_rect()

        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def draw(self, display):
        display.blit(self.image, (Environment.SCALE * self.pos[0], Environment.SCALE * self.pos[1]))
