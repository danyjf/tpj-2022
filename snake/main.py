import pygame
from food import Food
from snake import Snake
from environment import Environment
from game import Game

if __name__ == "__main__":
    pygame.init()
    
    g = Game()
    g.loop()
    
    pygame.quit()
