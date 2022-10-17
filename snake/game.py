import pygame

from environment import Environment
from snake import Snake
from food import Food
from input_handler import InputHandler
from observer import Observer

class Game(Observer):
    def __init__(self):
        self.display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.snake.add_observer(self)
        self.food = Food()
        self.input_handler = InputHandler()
        self.running = True
    
    def get_input(self, event):
        if event.key == pygame.K_w:
            self.input_handler.handle_input('w', self.snake)
        elif event.key == pygame.K_s:
            self.input_handler.handle_input('s', self.snake)
        elif event.key == pygame.K_a:
            self.input_handler.handle_input('a', self.snake)
        elif event.key == pygame.K_d:
            self.input_handler.handle_input('d', self.snake)
    
    def on_notify(self, entity, event):
        if event == Environment.EAT:
            entity.grow()
            self.food.randomize_pos()
        elif event == Environment.DIE:
            self.running = False
    
    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.get_input(event)

            # move snake
            self.snake.move()
            
            # snake collisions
            self.snake.check_collisions(self.food)

            # render
            self.display.fill("white")
            
            self.food.draw(self.display)
            self.snake.draw(self.display)

            pygame.display.flip()
            self.clock.tick(15)
