# import numpy as np
import pygame

from background import Background
from cells import Cells


class Game:
    def __init__(self, display_size, grid_size, name):
        self.__display_size = display_size
        self.__screen = pygame.display.set_mode((display_size[0], display_size[1]))

        self.__grid_size = grid_size

        self.__back_color = pygame.color.Color("white")
        self.__line_color = pygame.color.Color("grey")
        self.__alive_color = pygame.color.Color("black")
        self.__line_width = 2

        self.__background = Background(self.__screen, grid_size, self.__line_color, self.__line_width)
        self.__cells = Cells(self.__screen, grid_size, self.__back_color, self.__alive_color, self.__line_width)

        pygame.display.set_caption(name)
        self.__screen.fill(self.__back_color)

        self.__cells.Draw()
        self.__background.Draw()

        pygame.display.update()

    def Start(self):
        print("nothing yet")

    def Exit(self):
        print("nothing yet")

    def Move(self, offset):
        self.__screen.fill(self.__back_color)
        self.__cells.Move(offset)
        self.__background.Move(offset)
        pygame.display.update()

    def Update(self):
        print("nothing yet")

    def Tick(self):
        self.__screen.fill(self.__back_color)
        self.__cells.Switch_cell(0, 0)
        self.__cells.Switch_cell(1, 1)
        self.__cells.Switch_cell(2, 3)
        self.__cells.Switch_cell(4, 3)
        self.__cells.Draw()
        self.__background.Draw()
        # self.__cells.Step_up()

        pygame.display.update()
