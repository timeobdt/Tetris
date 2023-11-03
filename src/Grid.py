import pygame
from Line import Line
from constant import GRID_HEIGHT, GRID_WIDTH, ZERO, FRAME, screen
from Tetriminos import TetriminosFactory

pygame.init()

class Grid:

    def __init__(self):
        self.grid = [Line(row) for row in range(GRID_HEIGHT)]
        self.tetriminos = None
        self.x = None
        self.y = None
        self.change_tetriminos()
        self.draw_tetriminos()
        self.counter_frame = 0
        self.is_over = False
        self.score = 0
        self.font = pygame.font.Font('assets/font/bit5x3.ttf', 40)

    def change_tetriminos(self):
        self.tetriminos = TetriminosFactory.createRandom()
        self.x = GRID_WIDTH // 2
        self.y = 1
        self.is_over = not self.is_tetriminos_drawable()

    def reset(self):
        self.__init__()

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

    def is_game_over(self):
        return self.is_over

    def go_down(self):
        self.erase_tetriminos()
        self.y += 1
        if self.is_tetriminos_drawable():
            self.draw_tetriminos()
            return True
        else:
            self.y -= 1
            self.draw_tetriminos()
            self.change_tetriminos()
            self.update_lines()
            return False

    def is_tetriminos_drawable(self):
        for i in range(len(self.tetriminos)):
            for j in range(len(self.tetriminos[ZERO])):
                if (((self.y + i) not in range(GRID_HEIGHT) or
                     (self.x + j) not in range(GRID_WIDTH)) or
                        (self.grid[self.y + i].line[self.x + j].get() and
                            self.tetriminos[i][j])):
                    return False
        return True

    def is_line_complete(self, row):
        return self.grid[row].is_full()

    def horizontal_move(self, direction):
        self.erase_tetriminos()
        self.x += direction
        if self.is_tetriminos_drawable():
            self.draw_tetriminos()
        else:
            self.x -= direction
            self.draw_tetriminos()

    def place(self):
        while self.go_down():
            continue

    def rotate(self):
        self.erase_tetriminos()
        self.tetriminos = TetriminosFactory.rotate_right(self.tetriminos)
        if not self.is_tetriminos_drawable():
            self.tetriminos = TetriminosFactory.rotate_left(self.tetriminos)
        self.draw_tetriminos()

    def update_lines(self):
        line_delete_compter = 0
        for i in range(len(self.grid)):
            if self.is_line_complete(i):
                self.remove_line(i)
                line_delete_compter += 1
        if line_delete_compter == 4:
            self.score += 800
        if line_delete_compter == 3:
            self.score += 500
        if line_delete_compter == 2 :
            self.score += 300
        if line_delete_compter == 1 :
            self.score += 100

    def update(self):
        self.display_score()
        self.counter_frame += 1
        if not self.counter_frame % FRAME:
            self.go_down()

    def remove_line(self, row):
        for i in range(row, 1, -1):
            for column in range(1, GRID_WIDTH - 1):
                value = self.grid[i - 1].line[column].get()
                self.grid[i].line[column].set(value)
        self.grid[0] = Line(0)

    def display_score(self):
        score_surf = self.font.render(f"{self.score}", False, (255, 255, 255))
        score_rect = score_surf.get_rect(topleft=(200, 350))
        screen.blit(score_surf, score_rect)

    