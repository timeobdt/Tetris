import random


class TetriminosFactory:

    @staticmethod
    def createS():
        return [[0, 0, 0],
                [0, 1, 1],
                [1, 1, 0]]

    @staticmethod
    def createT():
        return [[2, 2, 2],
                [0, 2, 0],
                [0, 0, 0]]

    @staticmethod
    def createZ():
        return [[3, 3, 0],
                [0, 3, 3],
                [0, 0, 0]]

    @staticmethod
    def createJ():
        return [[0, 0, 4],
                [0, 0, 4],
                [0, 4, 4]]

    @staticmethod
    def createI():
        return [[0, 0, 0, 5],
                [0, 0, 0, 5],
                [0, 0, 0, 5],
                [0, 0, 0, 5]]

    @staticmethod
    def createL():
        return [[6, 0, 0],
                [6, 0, 0],
                [6, 6, 0]]

    @staticmethod
    def createO():
        return [[0, 0, 0],
                [7, 7, 0],
                [7, 7, 0]]

    @staticmethod
    def createRandom():
        all = [
            TetriminosFactory.createS(),
            TetriminosFactory.createZ(),
            TetriminosFactory.createO(),
            TetriminosFactory.createL(),
            TetriminosFactory.createJ(),
            TetriminosFactory.createT(),
            TetriminosFactory.createI()
        ]
        return random.choice(all)
