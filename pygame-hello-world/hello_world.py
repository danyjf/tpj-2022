import pygame as pygame
from pygame import *
from pygame.sprite import *
from among_us import AmongUs

pygame.init()
screen = display.set_mode((800, 600))
display.set_caption("Hello World")

hero = AmongUs()

all_sprites = pygame.sprite.Group()
all_sprites.add(hero)

while True:
    e = event.wait()
    if e.type == QUIT:
        pygame.quit()
        break
    
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    display.update()
