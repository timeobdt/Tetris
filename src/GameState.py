import pygame
from constant import RIGHT, LEFT, WHITE, WIDTH, HEIGHT, BLACK, backgroud_rect, background_surf, GRID_WIDTH_IN_WINDOW, GRID_HEIGHT_IN_WINDOW, GRID_POSITION_X, GRID_POSITION_Y
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
        GameContext.grid.reset()
        self.context.state = RunningGameState(self.context)

    def on_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next()

    def update(self):
        GameContext.screen.blit(background_surf, backgroud_rect)
        logo_width = 1000 / 3
        logo_height = 694 / 3
        logo_surf = pygame.transform.scale(pygame.image.load('assets/logo.png').convert_alpha(), (logo_width, logo_height) )
        logo_rect = logo_surf.get_rect()
        text = "Press space to start."
        font = pygame.font.Font('assets/font/bit5x3.ttf', 64)
        text_surface = font.render(text, False, WHITE)
        rect = text_surface.get_rect()
        x_text, y_text = (WIDTH - rect.w) // 2, (HEIGHT - rect.h + 100) // 2
        x_logo, y_logo = (WIDTH - logo_rect.w) // 2, (HEIGHT - logo_rect.h - 300) // 2
        GameContext.screen.blit(text_surface, (x_text, y_text))
        GameContext.screen.blit(logo_surf, (x_logo, y_logo))


class RunningGameState(GameState):

    def __init__(self, context):
        super().__init__(context)

    def next(self):
        self.context.state = PausedGameState(self.context)

    def update(self):
        GameContext.screen.blit(background_surf, backgroud_rect)
        pygame.draw.rect(GameContext.screen, BLACK, pygame.Rect(GRID_POSITION_X, GRID_POSITION_Y, GRID_WIDTH_IN_WINDOW, GRID_HEIGHT_IN_WINDOW))
        GameContext.grid.update()
        list_sprites.draw(GameContext.screen)
        if GameContext.grid.is_over:
            self.context.state = GameOverGameState(self.context)

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
        GameContext.screen.blit(background_surf, backgroud_rect)
        pause = "PAUSE"
        text = "press ESCAPE to resume."
        font = pygame.font.Font('assets/font/bit5x3.ttf', 64)
        pause_surface = font.render(pause, False, WHITE)
        text_surface = font.render(text, False, WHITE)
        rect = text_surface.get_rect()
        pause_rect = pause_surface.get_rect()
        x, y = (WIDTH - rect.w) // 2, (HEIGHT - rect.h) // 1.5
        GameContext.screen.blit(text_surface, (x, y))
        x, y = (WIDTH - pause_rect.w) // 2, (HEIGHT - pause_rect.h) // 3
        GameContext.screen.blit(pause_surface, (x, y))


class GameOverGameState(GameState):
    def __init__(self, context):
        super().__init__(context)

    def next(self):
        self.context.state = MenuGameState(self.context)

    def on_key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.next()

    def update(self):
        GameContext.screen.blit(background_surf, backgroud_rect)
        pause = "GAME OVER"
        text = "Press SPACE to return to the menu."
        font = pygame.font.Font('assets/font/bit5x3.ttf', 64)
        text_surface = font.render(text, False, WHITE)
        font = pygame.font.Font('assets/font/bit5x3.ttf', 128)
        pause_surface = font.render(pause, False, WHITE)
        rect = text_surface.get_rect()
        x, y = (WIDTH - rect.w) // 2, (HEIGHT - rect.h) // 1.5
        pause_rect = pause_surface.get_rect()
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
