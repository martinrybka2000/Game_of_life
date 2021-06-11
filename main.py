import pygame
# import numpy as np
from game import Game


pygame.init()

# image = pygame.Surface([20, 20]).convert_alpha()

game = Game((800, 800), (5, 5), "Game of life")

while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # keys presing handling
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    elif keys[pygame.K_LEFT]:
        game.Tick()

    # delay
    pygame.time.delay(10)
