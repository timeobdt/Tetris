from Line import Line
from constant import GRID_HEIGHT


class Grid:

    def __init__(self):
        self.grid = [Line(row) for row in range(GRID_HEIGHT)]
