import pygame
# import numpy as np
from game import Game


pygame.init()

# image = pygame.Surface([20, 20]).convert_alpha()

game = Game((800, 800), 10, "Game of life")

pygame.key.set_repeat(500, 20)

button_flag = True
button_flag2 = True

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

    elif keys[pygame.K_SPACE] and button_flag:
        game.Tick()
        # button_flag = False

    elif keys[pygame.K_SPACE] == False and button_flag == False:
        button_flag = True

    elif keys[pygame.K_d] and button_flag2:
        game.Start()
        button_flag2 = False

    elif keys[pygame.K_d] == False and button_flag2 == False:
        button_flag2 = True

        # delay
    pygame.time.delay(20)
