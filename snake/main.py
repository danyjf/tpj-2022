import pygame
import random
from food import Food
from snake import Snake
from environment import Environment

display = pygame.display.set_mode((Environment.SCALE * Environment.WIDTH, Environment.SCALE * Environment.HEIGHT))
clock = pygame.time.Clock()

snake = Snake()
food = Food()

Environment.running = True
while Environment.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Environment.running = False
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
            print(event.txt)
            
    display.fill("white")

    # move snake
    snake.move()
    
    food.draw(display)
    snake.draw(display, food)

    # update window
    pygame.display.flip()
    clock.tick(15)

pygame.quit()
