import pygame
import random
from food import Food
from snake import Snake
from environment import Environment

display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
clock = pygame.time.Clock()

snake = Snake()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.up()
            elif event.key == pygame.K_DOWN:
                snake.down()
            elif event.key == pygame.K_LEFT:
                snake.left()
            elif event.key == pygame.K_RIGHT:
                snake.right()
        elif event.type == Environment.GAME_EVENT:
            if event.name == 'collision':
                if event.obj == 'wall' or event.obj == 'snake':
                    running = False
                elif event.obj == 'food':
                    snake.grow()
                    food.randomize_pos()

    # move snake
    snake.move()
    
    # snake collisions
    snake.check_collisions(food)

    # render
    display.fill("white")
    
    food.draw(display)
    snake.draw(display)

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
