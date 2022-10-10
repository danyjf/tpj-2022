import pygame as pygame
from pygame import *
from pygame.sprite import *
from among_us import AmongUs

pygame.init()
screen = display.set_mode((800, 600))
display.set_caption("Hello World")

sprite_object = AmongUs("among_us_red.png", 100, 100)
sprite_object2 = AmongUs("among_us_lime.png", 300, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite_object)
all_sprites.add(sprite_object2)

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
                undo = (0, 20)
                sprite_object.update((0, -20))
            if key[K_DOWN]:
                undo = (0, -20)
                sprite_object.update((0, 20))
            if key[K_LEFT]:
                undo = (20, 0)
                sprite_object.update((-20, 0))
            if key[K_RIGHT]:
                undo = (-20, 0)
                sprite_object.update((20, 0))
    
    if sprite_object.rect.colliderect(sprite_object2.rect):
        sprite_object.update(undo)
        sprite_object2.update_sprite("among_us_lime_dead.png")
    
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    display.update()
