from Case import Case
from constant import GRID_WIDTH


class Line:

    def __init__(self, row: int):
        self.line = LineFactory.create_line(row)


class LineFactory:

    @staticmethod
    def create_line(row: int):
        return [Case('black', row, column) for column in range(GRID_WIDTH)]

