import pygame.image

from Sprite import Sprite
from constant import CASE_SIZE, GRID_POSITION_X, GRID_POSITION_Y, COLORS


class Case(Sprite):

    def __init__(self, color: str, row: int, column: int):
        self.path = f'assets/{color}.jpg'
        super().__init__(
            f'assets/{color}.jpg',
            column * CASE_SIZE + GRID_POSITION_X,
            row * CASE_SIZE + GRID_POSITION_Y
        )

    def set(self, value: int):
        self.path = f'assets/{COLORS[value]}.jpg'
        self.image = pygame.image.load(self.path).convert_alpha()

    def get(self):
        color = self.path.split('/')[1].split('.')[0]
        for k in COLORS.keys():
            if COLORS[k] == color:
                return k
