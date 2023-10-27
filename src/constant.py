WIDTH = 1280
HEIGHT = 720

GRID_WIDTH = 12
GRID_HEIGHT = 22
CASE_SIZE = 720 / (GRID_HEIGHT + 1)

GRID_WIDTH_IN_WINDOW = GRID_WIDTH * CASE_SIZE
GRID_POSITION_X = (WIDTH - GRID_WIDTH_IN_WINDOW) / 2

GRID_HEIGHT_IN_WINDOW = GRID_HEIGHT * CASE_SIZE
GRID_POSITION_Y = (HEIGHT - GRID_HEIGHT_IN_WINDOW) / 2

FRAME = 60
SPEED = CASE_SIZE / FRAME
ZERO = 0

COLORS = {
    0: 'black',
    1: 'yellow',
    2: 'red',
    3: 'purple',
    4: 'pink',
    5: 'spring_green',
    6: 'green',
    7: 'blue',
    8: 'grey'
}

RIGHT = 1
LEFT = -1

KEY_SPEED = 1.5
