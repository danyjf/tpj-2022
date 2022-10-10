import pygame as pygame
from pygame import *
from pygame.sprite import *

class AmongUs(Sprite):
    def __init__(self, location, x, y):
        Sprite.__init__(self)
        
        self.image = image.load(location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (170, 200))
        
        self.rect = Rect(x, y, 150, 150)
        
    def update_sprite(self, location):
        self.image = image.load(location).convert_alpha()
        self.image = pygame.transform.scale(self.image, (170, 200))
    
    def update(self, vector):
        x, y = vector
        self.rect = self.rect.move(x, y)
