import pygame
# import numpy as np
from game import Game


pygame.init()

# image = pygame.Surface([20, 20]).convert_alpha()

game = Game((800, 800), (5, 5), "Game of life")
button_flag = True

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
        game.Move((-10, 0))

    elif keys[pygame.K_RIGHT]:
        game.Move((10, 0))

    elif keys[pygame.K_UP]:
        game.Move((0, -10))

    elif keys[pygame.K_DOWN]:
        game.Move((0, 10))

    elif keys[pygame.K_a] and button_flag:
        game.Tick()
        button_flag = False

    elif keys[pygame.K_a] == False and button_flag == False:
        button_flag = True

        # delay
    pygame.time.delay(20)
