import pygame
import random

from const import SCALE

class Ant:
    def __init__(self):
        self.x = 40
        self.y = 20
    
    def update(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
    
    def render(self, display):
        pygame.draw.rect(display, 'black', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
