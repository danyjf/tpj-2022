import enum
import pygame
from enum import Enum

from environment import Environment
from subject import Subject

class SNAKE_STATES(Enum):
    MOVE = 1
    EAT = 2
    GROW = 3
    DIE = 4

class Snake(Subject):
    def __init__(self, name, posX, posY):
        super().__init__()
        self.name = name
        self.dead = False
        self.body = [(posX, posY), (posX - 1, posY), (posX - 2, posY)]
        self.direction = (1, 0)
        self.length = 3
        self.state = SNAKE_STATES.MOVE

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
    
    def kill(self):
        self.dead = True
    
    def death_collision(self):
        head = self.body[0]
        if head[0] not in range(Environment.WIDTH) or head[1] not in range(Environment.HEIGHT):
            return True

        for body in self.body[1:]:
            if head == body:
                return True
        return False

    def food_collision(self, food):
        head = self.body[0]
        for item in food:
            if item.pos == head:
                item.randomize_pos()
                self.notify(self, Environment.EAT)
                return True
        return False

    def update(self, food):
        if self.state == SNAKE_STATES.MOVE:
            self.move()
            if self.food_collision(food):
                self.state = SNAKE_STATES.EAT
            elif self.death_collision():
                self.state = SNAKE_STATES.DIE
        elif self.state == SNAKE_STATES.EAT:
            self.move()
            self.state = SNAKE_STATES.GROW
        elif self.state == SNAKE_STATES.GROW:
            self.move()
            self.grow()
            self.state = SNAKE_STATES.MOVE
        elif self.state == SNAKE_STATES.DIE:
            self.kill()

    def draw(self, display):
        for x, y in self.body:
            pygame.draw.rect(display, "red", (Environment.SCALE * x, Environment.SCALE * y, Environment.SCALE, Environment.SCALE))
