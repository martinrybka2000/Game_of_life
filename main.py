import pygame
import numpy as np
from Game import T_Game

pygame.init()
# definiowanie okna gry
# win = pygame.display.set_mode((500, 500))
# wyświetlenie okna gry


run = True

# image = pygame.Surface([20, 20]).convert_alpha()

game = T_Game((500, 500), (20, 20))

while run:
    # obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_ESCAPE]:
        run = False

    elif keys[pygame.K_LEFT]:
        # win.scroll(1, 1)
        # print(str(win.get_abs_offset()))
        # win.fill((255, 255, 255))
        # pygame.draw.line(win, (0, 255, 0), (-50 + cnt, 0),
        #  (200 + cnt, 200), 10)
        pygame.display.update()

    pygame.time.delay(50)
