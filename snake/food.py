import pygame
import random
from environment import Environment

class Food:
    def __init__(self):
        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def draw(self, display):
        pygame.draw.rect(display, "green", (Environment.SCALE * self.pos[0], Environment.SCALE * self.pos[1], Environment.SCALE, Environment.SCALE))
