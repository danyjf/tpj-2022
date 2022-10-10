import pygame as pygame
from pygame import *
from pygame.sprite import *
from among_us import AmongUs

pygame.init()
screen = display.set_mode((800, 600))
display.set_caption("Hello World")

sprite_object = AmongUs()

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite_object)

clock = pygame.time.Clock()

while True:
    clock.tick(24)
    
    for e in event.get():
        if e.type == QUIT:
            pygame.quit()
            break
        elif e.type == KEYDOWN:
            key = pygame.key.get_pressed()
            if key[K_UP]:
                sprite_object.update((0, -20))
            if key[K_DOWN]:
                sprite_object.update((0, 20))
            if key[K_LEFT]:
                sprite_object.update((-20, 0))
            if key[K_RIGHT]:
                sprite_object.update((20, 0))
    
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    display.update()
