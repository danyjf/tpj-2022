import pygame
import random

from const import SCALE
from entity import Entity

class Ant(Entity):
    def __init__(self):
        self.x = 50
        self.y = 30
    
    def update(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
    
    def render(self, display):
        pygame.draw.rect(display, 'black', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
