import pygame

from sys import exit
from Util import list_sprites
from Grid import Grid

from constant import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
grid = Grid()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    list_sprites.draw(screen)
    pygame.display.update()
