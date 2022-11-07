import pygame

from environment import Environment
from snake import Snake
from apple import Apple
from input_handler import InputHandler
from spawner import Spawner
from score_board import ScoreBoard

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
        self.clock = pygame.time.Clock()
        self.input_handler = InputHandler()
        self.running = True
        
        self.snakes = [Snake('Player1', 40, 10), Snake('Player2', 40, 30)]
        # self.snakes = [Snake('Player1', 40, 10)]

        self.score_board = ScoreBoard(self.snakes)
        
        self.spawner = Spawner()
        apple = Apple()
        self.food = [
            self.spawner.spawn_food(apple), 
            self.spawner.spawn_food(apple)
        ]
    
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
    
    def render(self):
        self.display.fill("white")
            
        for item in self.food:
            item.draw(self.display)
        for snake in self.snakes:
            snake.draw(self.display)
        self.score_board.draw(self.display)
            
        pygame.display.flip()

    def update(self):
        for snake in self.snakes:
            snake.update(self.food)
    
    def loop(self):
        while not any(snake.dead for snake in self.snakes):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    [snake.kill() for snake in self.snakes]
                elif event.type == pygame.KEYDOWN:
                    self.get_input(event)

            self.update()

            self.render()
            
            self.clock.tick(15)
