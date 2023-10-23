from Sprite import Sprite
from constant import CASE_SIZE


class Case(Sprite):

    def __init__(self, color: str, row: int, column: int):
        super().__init__(f'assets/{color}.jpg', column * CASE_SIZE, row * CASE_SIZE)
