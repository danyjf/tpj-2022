import pygame
from environment import Environment
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
    
    def loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.down()
                    elif event.key == pygame.K_LEFT:
                        self.snake.left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.right()
                elif event.type == Environment.GAME_EVENT:
                    if event.name == 'collision':
                        if event.obj == 'wall' or event.obj == 'snake':
                            running = False
                        elif event.obj == 'food':
                            self.snake.grow()
                            self.food.randomize_pos()

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
