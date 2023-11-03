import pygame

from sys import exit
from Util import list_sprites
from Grid import Grid
from constant import WIDTH, HEIGHT, FRAME, RIGHT, LEFT, KEY_SPEED
from GameState import GameContext

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tetris')
clock = pygame.time.Clock()
grid = Grid()
counter = 0
state = GameContext()
GameContext.grid = grid
GameContext.screen = screen

while True:
    counter += 1
    clock.tick(FRAME)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            counter = 0
    if counter % KEY_SPEED == 0:
        state.on_key_pressed()
    state.update()
    pygame.display.update()
