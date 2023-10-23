import pygame
from Util import list_sprites


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image: str, x: int, y: int):
        super(Sprite, self).__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        list_sprites.add(self)
