import pygame

from sys import exit

from constant import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.display.update() #update frame
    clock.tick(60) #adjust the framerate