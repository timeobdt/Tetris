from Case import Case
from constant import GRID_WIDTH, GRID_HEIGHT


class Line:

    def __init__(self, row: int):
        self.line = LineFactory.create_line(row)


class LineFactory:

    @staticmethod
    def create_line(row: int):
        return [Case('grey', row, column) for column in range(GRID_WIDTH)]

