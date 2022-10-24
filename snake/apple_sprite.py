import pygame

from environment import Environment

class AppleSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (Environment.SCALE, Environment.SCALE))
        self.rect = self.image.get_rect()
