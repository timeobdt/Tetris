import pygame.time

from Line import Line
from constant import GRID_HEIGHT, GRID_WIDTH, ZERO
from Tetriminos import TetriminosFactory


class Grid:

    def __init__(self):
        self.grid = [Line(row) for row in range(GRID_HEIGHT)]
        self.tetriminos = None
        self.x = None
        self.y = None
        self.change_tetriminos()

    def change_tetriminos(self):
        self.tetriminos = TetriminosFactory.createRandom()
        self.x = GRID_WIDTH // 2
        self.y = ZERO

    def set(self, row, column, value):
        self.grid[row].line[column].set(value)

    def draw_tetriminos(self):
        for i in range(len(self.tetriminos[ZERO])):
            for j in range(len(self.tetriminos)):
                self.set(self.y + j, self.x + i, self.tetriminos[j][i])

    def erase_tetriminos(self):
        for i in range(len(self.tetriminos[ZERO])):
            for j in range(len(self.tetriminos)):
                if self.tetriminos[j][i] != ZERO:
                    self.set(self.y + j, self.x + i, ZERO)

    def go_down(self):
        self.erase_tetriminos()
        self.y += 1
        self.draw_tetriminos()