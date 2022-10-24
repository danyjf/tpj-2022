import pygame
import random

from environment import Environment
from food_sprite import FoodSprite

class Food:
    def __init__(self):
        self.food_sprite = FoodSprite()
        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def randomize_pos(self):
        self.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

    def draw(self, display):
        display.blit(self.food_sprite.image, (Environment.SCALE * self.pos[0], Environment.SCALE * self.pos[1]))
