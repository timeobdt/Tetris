import pygame.image

from Sprite import Sprite
from constant import CASE_SIZE, GRID_POSITION_X, GRID_POSITION_Y, COLORS


class Case(Sprite):

    def __init__(self, color: str, row: int, column: int):
        super().__init__(
            f'assets/{color}.jpg',
            column * CASE_SIZE + GRID_POSITION_X,
            row * CASE_SIZE + GRID_POSITION_Y
        )

    def set(self, value: int):
        self.image = pygame.image.load(f'assets/{COLORS[value]}.jpg').convert_alpha()
