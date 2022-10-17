import pygame

from environment import Environment
from subject import Subject

class Snake(Subject):
    def __init__(self, posX, posY):
        super().__init__()
        self.body = [(posX, posY), (posX - 1, posY), (posX - 2, posY)]
        self.direction = (1, 0)
        self.length = 3

    def up(self):
        if self.direction != (0, 1):
            self.direction = (0, -1)

    def down(self):
        if self.direction != (0, -1):
            self.direction = (0, 1)

    def left(self):
        if self.direction != (1, 0):
            self.direction = (-1, 0)

    def right(self):
        if self.direction != (-1, 0):
            self.direction = (1, 0)

    def move(self):
        self.body[0:0] = [
            (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        ]
        while len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1
        
    def check_collisions(self, food):
        for x, y in self.body:
            if food.pos == (x, y):
                self.notify(self, Environment.EAT)

            if x not in range(Environment.WIDTH) or y not in range(Environment.HEIGHT):
                self.notify(self, Environment.DIE)

            if self.body.count((x, y)) > 1:
                self.notify(self, Environment.DIE)

    def draw(self, display):
        for x, y in self.body:
            pygame.draw.rect(display, "red", (Environment.SCALE * x, Environment.SCALE * y, Environment.SCALE, Environment.SCALE))
