import pygame

from sys import exit
from Util import list_sprites
from Grid import Grid

from constant import WIDTH, HEIGHT, FRAME, RIGHT, LEFT, KEY_SPEED, screen

pygame.init()
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
grid = Grid()
counter = 0

while True:
    counter += 1
    clock.tick(FRAME)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if counter % KEY_SPEED == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            grid.horizontal_move(RIGHT)
        elif keys[pygame.K_LEFT]:
            grid.horizontal_move(LEFT)
        elif keys[pygame.K_DOWN]:
            grid.go_down()
        elif keys[pygame.K_SPACE]:
            grid.place()
        elif keys[pygame.K_UP]:
            grid.rotate()

    screen.fill((10, 10, 10))
    grid.update()
    list_sprites.draw(screen)
    pygame.display.update()
