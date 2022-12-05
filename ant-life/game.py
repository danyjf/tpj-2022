import pygame

from const import WIDTH, HEIGHT, SCALE
from ant import Ant
from home import Home
from food import Food

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
        self.clock = pygame.time.Clock()
        self.ant = Ant()
        self.home = Home()
        self.food = Food()
        self.game_objects = [self.ant, self.home, self.food]
    
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            for obj in self.game_objects:
                self.ant.check_collision(obj)

            self.update()
            
            self.render()
            
            self.clock.tick(15)
    
    def update(self):
        for obj in self.game_objects:
            obj.update()
    
    def render(self):
        self.display.fill("white")
        
        for obj in self.game_objects:
            obj.render(self.display)
        
        pygame.display.flip()
