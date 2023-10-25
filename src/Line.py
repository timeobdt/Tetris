from Case import Case
from constant import GRID_WIDTH, GRID_HEIGHT, ZERO


class Line:

    def __init__(self, row: int):
        self.line = LineFactory.create_static_line(row)


class LineFactory:

    @staticmethod
    def create_static_line(row: int):
        if row == ZERO or row == (GRID_HEIGHT - 1):
            return LineFactory.create_line_border(row)
        return LineFactory.create_line(row)

    @staticmethod
    def create_line(row: int):
        return [Case('grey' if column == ZERO or column == (GRID_WIDTH - 1) else 'black', row, column) for column in range(GRID_WIDTH)]

    @staticmethod
    def create_line_border(row: int):
        return [Case('grey', row, column) for column in range(GRID_WIDTH)]

            

