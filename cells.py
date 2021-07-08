
import numpy as np
import pygame
import math
import random
import time


class Cell:
    def __init__(self, n, alive):
        self.n = n
        self.alive = alive


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

        self.__alive_cells = {}
        self.__offset = [0, 0]
        self.__zoom = 0

        self.__myfont = pygame.font.SysFont('Comic Sans MS', 50)

        # for i in range(1000):
        # self.__alive_cells[(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))] = Cell(0, True)

    def __Judge_cells(self):
        # rules of the game of life
        for coord, cell in list(self.__alive_cells.items()):
            if (cell.alive == True):
                if (cell.n < 2 or cell.n > 3):
                    del self.__alive_cells[coord]
            elif (cell.n != 3):
                del self.__alive_cells[coord]

    def Increment_grid_size(self):
        self.__grid_size += 2

    def Decrement_grid_size(self):
        if (self.__grid_size > 2):
            self.__grid_size -= 2

    def Draw(self):

        offset = self.__offset

        # calculating cell size
        rec_width = self.__screen.get_width() / self.__grid_size
        rec_height = self.__screen.get_height() / self.__grid_size

        # drawing alive cells
        for coord, cell in self.__alive_cells.items():
            rect = pygame.Rect(coord[0]*rec_width + offset[0], coord[1]*rec_height + offset[1], rec_width, rec_height)
            pygame.draw.rect(self.__screen, self.__alive_color, rect)

        # drawing the alive cells counter
        textsurface = self.__myfont.render(str(len(self.__alive_cells)), False, (0, 0, 0))
        self.__screen.blit(textsurface, (5, self.__screen.get_height() - self.__myfont.get_height()))

    def Move(self, offset):
        # adding the offset and drawing the ceels again
        for i in range(len(offset)):
            self.__offset[i] += offset[i]

    def Step_up(self, num_of_steps):

        # t0 = time.clock_gettime(1)

        new_cells = {}

        for coord in self.__alive_cells:
            new_cells[coord] = Cell(0, True)

        for coord in self.__alive_cells:

            for x_dif, y_dif in ([-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]):
                if((coord[0] + x_dif, coord[1] + y_dif) in new_cells):
                    new_cells[(coord[0] + x_dif, coord[1] + y_dif)].n += 1
                else:
                    new_cells[(coord[0] + x_dif, coord[1] + y_dif)] = Cell(1, False)

        self.__alive_cells = new_cells

        self.__Judge_cells()

        # t1 = time.clock_gettime(1) - t0
        # print("Time elapsed: ", t1, "  cells cnt: ", len(self.__alive_cells))
        return self.__grid_size

    def Step_back(self, num_of_steps):
        print("nothing")

    def Switch_cell(self, x, y):
        # check if out of boundries
        if((x, y) in self.__alive_cells):
            del self.__alive_cells[x, y]
        else:
            self.__alive_cells[x, y] = Cell(0, True)

    def Turn_on_off_cell(self, x, y, on_off=True):
        # check if out of boundries
        if(on_off):
            if ((x, y) not in self.__alive_cells):
                self.__alive_cells[(x, y)] = Cell(0, True)
        else:
            self.__alive_cells.pop((x, y), False)

    def Get_grid_size(self):
        return self.__grid_size
