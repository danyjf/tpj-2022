import pygame

from const import WIDTH, HEIGHT, SCALE
from ant import Ant

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_objects = [Ant()]
    
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

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
