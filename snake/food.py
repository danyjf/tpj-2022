import random

from environment import Environment

class Food:
    def __init__(self):
        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def randomize_pos(self):
        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def draw(self):
        return NotImplemented

    def clone(self):
        return NotImplemented
