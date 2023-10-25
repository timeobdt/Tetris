from Line import Line
from constant import GRID_HEIGHT, GRID_WIDTH, ZERO, FRAME
from Tetriminos import TetriminosFactory


class Grid:

    def __init__(self):
        self.grid = [Line(row) for row in range(GRID_HEIGHT)]
        self.tetriminos = None
        self.x = None
        self.y = None
        self.change_tetriminos()
        self.draw_tetriminos()
        self.counter_frame = 0

    def change_tetriminos(self):
        self.tetriminos = TetriminosFactory.createRandom()
        self.x = GRID_WIDTH // 2
        self.y = ZERO

    def set(self, row, column, value):
        self.grid[row].line[column].set(value)

    def draw_tetriminos(self):
        for i in range(len(self.tetriminos)):
            for j in range(len(self.tetriminos[ZERO])):
                if self.tetriminos[i][j]:
                    self.set(self.y + i, self.x + j, self.tetriminos[i][j])

    def erase_tetriminos(self):
        for i in range(len(self.tetriminos)):
            for j in range(len(self.tetriminos[ZERO])):
                if self.tetriminos[i][j] != ZERO:
                    self.set(self.y + i, self.x + j, ZERO)

    def go_down(self):
        self.erase_tetriminos()
        self.y += 1
        if self.is_tetriminos_drawable():
            self.draw_tetriminos()
        else:
            self.y -= 1
            self.draw_tetriminos()
            self.change_tetriminos()

    def is_tetriminos_drawable(self):
        for i in range(len(self.tetriminos)):
            for j in range(len(self.tetriminos[ZERO])):
                if (((self.y + i) not in range(GRID_HEIGHT) or
                     (self.x + j) not in range(GRID_WIDTH)) or
                        (self.grid[self.y + i].line[self.x + j].get() and
                            self.tetriminos[i][j])):
                    return False
        return True

    def update(self):
        self.counter_frame += 1
        if not self.counter_frame % FRAME:
            self.go_down()
