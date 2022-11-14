import pygame
import random

from const import SCALE, WIDTH, HEIGHT
from entity import Entity

class Food(Entity):
    def __init__(self):
        self.x = random.randrange(0, WIDTH + 1)
        self.y = random.randrange(0, HEIGHT + 1)
    
    def update(self):
        pass
    
    def render(self, display):
        pygame.draw.rect(display, 'green', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
