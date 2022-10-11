import pygame
import random
from environment import Environment

class Snake:
    def __init__(self):
        self.body = [(40, 20), (39, 20), (38, 20)]
        self.direction = (1, 0)
        self.length = 3

    def up(self):
        self.direction = (0, -1)
    
    def down(self):
        self.direction = (0, 1)
    
    def left(self):
        self.direction = (-1, 0)
    
    def right(self):
        self.direction = (1, 0)
        
    def move(self):
        self.body[0:0] = [
            (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        ]
        while len(self.body) > self.length:
            self.body.pop()
        
    def draw(self, display, food):
        for x, y in self.body:
            pygame.draw.rect(display, "red", (Environment.SCALE * x, Environment.SCALE * y, Environment.SCALE, Environment.SCALE))

            if food.pos == (x, y):
                self.length += 1
                ev = pygame.event.Event(Environment.GAME_EVENT, {'txt': "mmmnhami"})
                pygame.event.post(ev)
                print("Sent")
                ev = pygame.event.Event(Environment.GAME_EVENT, {'txt': "dammmm"})
                pygame.event.post(ev)
                food.pos = (random.randrange(Environment.WIDTH), random.randrange(Environment.HEIGHT))

            if x not in range(Environment.WIDTH) or y not in range(Environment.HEIGHT):
                print("Snake crashed against the wall")
                Environment.running = False

            if self.body.count((x, y)) > 1:
                print("Snake eats self")
                Environment.running = False
