
import numpy as np
import pygame


class Cells:
    def __init__(self, surface, grid_size, back_color, alive_color, line_width):
        self.__screen = surface
        self.__display_size = surface.get_size()
        self.__grid_size = grid_size
        self.__back_color = back_color
        self.__alive_color = alive_color
        self.__line_width = line_width

        self.__number_of_steps = 10
        self.__actual_step = 0

        # self.__cells = [grid_size[0]][grid_size[1]][number_of_steps]
        self.__cells = np.zeros((grid_size[0], grid_size[1], self.__number_of_steps))
        self.__offset = [0, 0]
        self.__zoom = 0

        self.__cells[2][1][0] = True
        self.__cells[0][0][0] = True
        self.__cells[4][4][0] = True

    def Set_grid_size(self, grid_size):
        self.__grid_size = grid_size
        self.Draw()

    def Draw(self):

        offset = self.__offset

        # list of alive cells
        alivecells = []

        # calculating cell size
        rec_width = self.__screen.get_width() / self.__grid_size[0]
        rec_height = self.__screen.get_height() / self.__grid_size[1]

        # looking for alive cells
        for x in range(self.__cells.shape[0]):
            for y in range(self.__cells.shape[1]):
                if (self.__cells[x][y][0] == True):
                    alivecells.append(pygame.Rect(x*rec_width + offset[0], y*rec_height + offset[1], rec_width, rec_height))

        # drawing alive cells
        for rect in alivecells:
            pygame.draw.rect(self.__screen, self.__alive_color, rect)

    def Move(self, offset):
        # adding the offset and drawing the ceels again
        for i in range(len(offset)):
            self.__offset[i] += offset[i]
        self.Draw()

    def Step_up(self, num_of_steps):
        print("nothing")

    def Step_back(self, num_of_steps):
        print("nothing")

    def Switch_cell(self, xy):
        print("nothing")
