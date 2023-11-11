import random
from constant import ZERO

class TetriminosFactory:

    @staticmethod
    def createS():
        return [[0, 1, 1],
                [1, 1, 0]]

    @staticmethod
    def createT():
        return [[2, 2, 2],
                [0, 2, 0]]

    @staticmethod
    def createZ():
        return [[3, 3, 0],
                [0, 3, 3]]

    @staticmethod
    def createJ():
        return [[0, 4],
                [0, 4],
                [4, 4]]

    @staticmethod
    def createI():
        return [[5],
                [5],
                [5],
                [5]]

    @staticmethod
    def createL():
        return [[6, 0],
                [6, 0],
                [6, 6]]

    @staticmethod
    def createO():
        return [[7, 7],
                [7, 7]]
    
    stack = []
    
    @staticmethod
    def reset_stack():
        TetriminosFactory.stack = [
            TetriminosFactory.createS(),
            TetriminosFactory.createZ(),
            TetriminosFactory.createO(),
            TetriminosFactory.createL(),
            TetriminosFactory.createJ(),
            TetriminosFactory.createT(),
            TetriminosFactory.createI()
        ]
        
    @staticmethod
    def createRandom():
        if not TetriminosFactory.stack:
            TetriminosFactory.reset_stack()
            return TetriminosFactory.createRandom()
        else:   
            element = random.choice(TetriminosFactory.stack)
            TetriminosFactory.stack.remove(element)
            return element

    @staticmethod
    def create_copy(tetriminos):
        copy = []
        for line in tetriminos:
            copy.append(line[:])
        return copy

    """
    [1, 1, 1] => [0, 1] => [0, 1, 0]
    [0, 1, 0] => [1, 1] => [1, 1, 1]
              => [0, 1] => 
    """


    """
    [3, 3, 3] => [0, 0]
    [0, 3, 0] => [0, 0]
              => [0, 0]
    """

    @staticmethod
    def create_empty(height, width):
        return [[0 for _ in range(width)] for _ in range(height)]

    @staticmethod
    def rotate_right(tetriminos):
        copy = TetriminosFactory.create_empty(len(tetriminos[ZERO]), len(tetriminos))
        h, w = len(copy[ZERO]), len(copy)
        for i in range(h):
            for j in range(w):
                copy[j][h-i-1] = tetriminos[i][j]
        return copy

    @staticmethod
    def rotate_left(tetriminos):
        copy = TetriminosFactory.create_copy(tetriminos)
        for i in range(3):
            copy = TetriminosFactory.rotate_right(copy)
        return copy
