import pygame

from sys import exit
from Util import list_sprites
from Grid import Grid

from constant import WIDTH, HEIGHT, FRAME

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

    grid.update()
    list_sprites.draw(screen)
    pygame.display.update()
