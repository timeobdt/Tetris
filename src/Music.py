import pygame


class MusicPlayer:
    def playA(self):
        pygame.mixer_music.load("assets/music/Tetris-Tetris-Theme-(Lofi-Lia-Remix).wav")
        pygame.mixer_music.play(-1)
