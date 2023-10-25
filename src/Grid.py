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
        self.y = 1

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
            return True
        else:
            self.y -= 1
            self.draw_tetriminos()
            
            for i in range(len(self.tetriminos)):
                if self.is_line_complete(self.y + i):
                    self.remove_line(self.y + i)
                
            self.change_tetriminos()
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

    def update(self):
        self.counter_frame += 1
        if not self.counter_frame % FRAME:
            self.go_down()
            
    def is_line_complete(self, row):
        for column in range(1, GRID_WIDTH - 1):  
            if self.grid[row].line[column].get() == ZERO:
                return False
        return True
    
    def remove_line(self, row):
        for i in range(row, 1, -1):
            for column in range(1, GRID_WIDTH - 1):
                value = self.grid[i - 1].line[column].get()
                self.grid[i].line[column].set(value)
        self.grid[0] = Line(0)
    
        


    