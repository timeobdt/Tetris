import pygame
from constant import RIGHT, LEFT, WHITE, WIDTH, HEIGHT, BLACK
from Util import list_sprites


class GameState:

    def __init__(self, context):
        self.context = context

    def next(self):
        pass

    def on_key_pressed(self):
        pass

    def update(self):
        pass


class MenuGameState(GameState):

    def __init__(self, context):
        super().__init__(context)

    def next(self):
        self.context.state = RunningGameState(self.context)

    def on_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next()

    def update(self):
        text = "Veuillez presser SPACE pour jouer."
        font = pygame.font.SysFont('Arial', 64)
        text_surface = font.render(text, False, WHITE)
        rect = text_surface.get_rect()
        x, y = (WIDTH - rect.w) // 2, (HEIGHT - rect.h) // 2
        GameContext.screen.blit(text_surface, (x, y))


class RunningGameState(GameState):

    def __init__(self, context):
        super().__init__(context)

    def next(self):
        self.context.state = PausedGameState(self.context)

    def update(self):
        GameContext.grid.update()
        GameContext.screen.fill((10, 10, 10))
        list_sprites.draw(GameContext.screen)

    def on_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            GameContext.grid.horizontal_move(RIGHT)
        elif keys[pygame.K_LEFT]:
            GameContext.grid.horizontal_move(LEFT)
        elif keys[pygame.K_DOWN]:
            GameContext.grid.go_down()
        elif keys[pygame.K_SPACE]:
            GameContext.grid.place()
        elif keys[pygame.K_UP]:
            GameContext.grid.rotate()
        elif keys[pygame.K_ESCAPE]:
            self.next()


class PausedGameState(GameState):
    def __init__(self, context):
        super().__init__(context)

    def next(self):
        self.context.state = RunningGameState(self.context)

    def on_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.next()

    def update(self):
        GameContext.screen.fill(BLACK)
        pause = "PAUSE"
        text = "Veuillez presser ESCAPE pour reprendre."
        font = pygame.font.SysFont('Arial', 128)
        pause_surface = font.render(pause, False, WHITE)
        font = pygame.font.SysFont('Arial', 64)
        text_surface = font.render(text, False, WHITE)
        rect = text_surface.get_rect()
        pause_rect = pause_surface.get_rect()
        x, y = (WIDTH - rect.w) // 2, (HEIGHT - rect.h) // 1.5
        GameContext.screen.blit(text_surface, (x, y))
        x, y = (WIDTH - pause_rect.w) // 2, (HEIGHT - pause_rect.h) // 3
        GameContext.screen.blit(pause_surface, (x, y))


class GameContext:

    grid = None
    screen = None

    def __init__(self):
        self.state = MenuGameState(self)

    def next(self):
        self.state.next()

    def on_key_pressed(self):
        self.state.on_key_pressed()

    def update(self):
        self.state.update()
