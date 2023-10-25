import pygame

from sys import exit
from Util import list_sprites
from Grid import Grid

from constant import WIDTH, HEIGHT, FRAME, RIGHT, LEFT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
grid = Grid()
while True:
    clock.tick(FRAME)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                grid.horizontal_move(RIGHT)
            elif keys[pygame.K_LEFT]:
                grid.horizontal_move(LEFT)
            elif keys[pygame.K_DOWN]:
                grid.go_down()
            elif keys[pygame.K_SPACE]:
                grid.place()

    grid.update()
    screen.fill((10, 10, 10))
    list_sprites.draw(screen)
    pygame.display.update()
