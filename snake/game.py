import pygame

from environment import Environment
from snake import Snake
from apple import Apple
from input_handler import InputHandler
from observer import Observer

class Game(Observer):
    def __init__(self):
        self.display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
        self.clock = pygame.time.Clock()
        # self.snakes = [Snake(40, 10), Snake(40, 30)]
        self.snakes = [Snake(40, 10)]
        for snake in self.snakes:
            snake.add_observer(self)
        apple = Apple()
        self.food = [apple, apple.clone()]
        self.input_handler = InputHandler()
        self.running = True
    
    def get_input(self, event):
        if event.key == pygame.K_w:
            self.input_handler.handle_input('w', self.snakes[0])
        elif event.key == pygame.K_s:
            self.input_handler.handle_input('s', self.snakes[0])
        elif event.key == pygame.K_a:
            self.input_handler.handle_input('a', self.snakes[0])
        elif event.key == pygame.K_d:
            self.input_handler.handle_input('d', self.snakes[0])
        elif event.key == pygame.K_UP:
            self.input_handler.handle_input('up', self.snakes[-1])
        elif event.key == pygame.K_DOWN:
            self.input_handler.handle_input('down', self.snakes[-1])
        elif event.key == pygame.K_LEFT:
            self.input_handler.handle_input('left', self.snakes[-1])
        elif event.key == pygame.K_RIGHT:
            self.input_handler.handle_input('right', self.snakes[-1])
    
    def on_notify(self, entity, event):
        if event == Environment.EAT:
            entity[0].grow()
            entity[1].randomize_pos()
        elif event == Environment.DIE:
            self.running = False
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.get_input(event)

            # move snake and check collisions
            for snake in self.snakes:
                snake.move()
                snake.check_collisions(self.food)

            # render
            self.display.fill("white")
            
            for item in self.food:
                item.draw(self.display)
            for snake in self.snakes:
                snake.draw(self.display)

            pygame.display.flip()
            self.clock.tick(15)
