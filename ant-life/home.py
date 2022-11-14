import pygame

from const import SCALE
from entity import Entity

class Home(Entity):
    def __init__(self):
        self.x = 40
        self.y = 20
        self.water = 0
        self.food = 0
    
    def update(self):
        pass
    
    def render(self, display):
        pygame.draw.rect(display, 'orange', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
