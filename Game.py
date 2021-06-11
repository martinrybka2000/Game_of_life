# import numpy as np
import pygame

from background import Background
from cells import Cells


class T_Game:
    def __init__(self, display_size, grid_size):
        self.__display_size = display_size
        self.__grid_size = grid_size
        self.__screen = pygame.display.set_mode(
            (display_size[0], display_size[1]))
        self.__background = Background
        self.__cells = Cells

        pygame.display.set_caption("GOL")
        self.__screen.fill((255, 255, 255))

        pygame.display.update()

    def Start(self):
        print("nothing yet")

    def Exit(self):
        print("nothing yet")

    def Update(self):
        print("nothing yet")

    def Tick(self):
        print("nothing yet")
