import pygame
import random

from const import SCALE, WIDTH, HEIGHT
from entity import Entity

class Ant(Entity):
    def __init__(self):
        self.x = 40
        self.y = 20
        self.resource = None
        self.directions = [self.up, self.down, self.left, self.right]
    
    def update(self):
        move = random.choice(self.directions)
        move()
    
    def up(self):
        self.y += 1
        
        if self.y < 0:
            self.y = 0
        
    def down(self):
        self.y -= 1
        
        if self.y > HEIGHT:
            self.y = HEIGHT
    
    def left(self):
        self.x -= 1
        
        if self.x < 0:
            self.x = 0
        
    def right(self):
        self.x += 1
        
        if self.x > WIDTH:
            self.x = WIDTH

    def render(self, display):
        pygame.draw.rect(display, 'black', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
