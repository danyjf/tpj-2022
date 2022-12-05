import pygame
import random

from const import SCALE, WIDTH, HEIGHT
from entity import Entity
from fsm import FSM, Search, GoHome, Transition

class Ant(Entity):
    def __init__(self):
        self.x = 40
        self.y = 20
        self.resource = None
        self.directions = [self.up, self.down, self.left, self.right]
        search = Search()
        go_home = GoHome()
        states = [search, go_home]
        transitions = {
            "collected_resource": Transition(search, go_home),
            "deposited_resource": Transition(go_home, search)
        }
        self.fsm = FSM(states, transitions)
        self.event = None
    
    def update(self):
        self.fsm.update(self.event, self)
    
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
            
    def search(self):
        random.choice(self.directions)()
        
    def check_collision(self, entity):
        if self.x == entity.x and self.y == entity.y and self != entity:
            if entity.__class__.__name__ == 'Food':
                self.event = 'collected_resource'

    def render(self, display):
        pygame.draw.rect(display, 'black', (SCALE * self.x, SCALE * self.y, SCALE, SCALE))
