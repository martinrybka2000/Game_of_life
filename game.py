# import numpy as np
import pygame
import math

from background import Background
from cells import Cells


class Game:
    def __init__(self, display_size, grid_size, name):
        self.__display_size = display_size
        self.__screen = pygame.display.set_mode((display_size[0], display_size[1]))

        # self.__grid_size = grid_size

        self.__back_color = pygame.color.Color("white")
        self.__line_color = pygame.color.Color("grey")
        self.__alive_color = pygame.color.Color("black")
        self.__line_width = 2
        self.__offset = [0, 0]

        self.__background = Background(self.__screen, grid_size, self.__line_color, self.__line_width)
        self.__cells = Cells(self.__screen, grid_size, self.__back_color, self.__alive_color, self.__line_width)

        pygame.display.set_caption(name)
        self.__screen.fill(self.__back_color)

        self.__cells.Draw()
        self.__background.Draw()

        pygame.display.update()

    def Start(self):
        if (self.__cells.Decrement_grid_size()):
            self.__screen.fill(self.__back_color)
            self.__background.Decrement_grid_size()
            self.__cells.Draw()
            self.__background.Draw()

            pygame.display.update()

    def Exit(self):
        print("nothing yet")

    def Move(self, offset):
        self.__cells.Move(offset)
        self.__background.Move(offset)

        for i in range(len(offset)):
            self.__offset[i] += offset[i]

        self.Update()

    def Update(self):
        self.__screen.fill(self.__back_color)
        self.__cells.Draw()
        self.__background.Draw()
        pygame.display.update()

    def Tick(self):
        self.__cells.Step_up(0)
        # self.__background.Set_grid_size(size)
        self.Update()

    def Click(self, x, y, moving=False, special_key=pygame.KMOD_NONE):

        x_pos = math.floor(((x - self.__offset[0]) * self.__cells.Get_grid_size()) / self.__display_size[0])
        y_pos = math.floor(((y - self.__offset[1]) * self.__cells.Get_grid_size()) / self.__display_size[1])

        if (not moving):
            self.__cells.Switch_cell(x_pos, y_pos)
        elif (special_key == pygame.KMOD_NONE):
            self.__cells.Turn_on_off_cell(x_pos, y_pos, True)
        elif (special_key == pygame.KMOD_LSHIFT):
            self.__cells.Turn_on_off_cell(x_pos, y_pos, False)

        self.Update()

    def Zoom(self, zoom):

        if(zoom > 0):
            self.__cells.Increment_grid_size()
            self.__background.Increment_grid_size()
        else:
            self.__cells.Decrement_grid_size()
            self.__background.Decrement_grid_size()

        self.Update()
