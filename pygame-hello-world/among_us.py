import pygame as pygame
from pygame import *
from pygame.sprite import *

class AmongUs(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = image.load("among_us.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (170, 200))
        self.rect = Rect(100, 100, 200, 200)
    
    def update(self, vector):
        x, y = vector
        self.rect = self.rect.move(x, y)
