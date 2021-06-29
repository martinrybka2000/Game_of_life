
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

        for i in range(100):
            self.__alive_cells[(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))] = Cell(0, True)

    def __Judge_cells(self):
        # rules of the game of life

        for coord, cell in list(self.__alive_cells.items()):
            if (cell.alive == True):
                if (cell.n < 2 or cell.n > 3):
                    del self.__alive_cells[coord]
            elif (cell.n != 3):
                del self.__alive_cells[coord]

    def Set_grid_size(self, grid_size):
        # calculate the diference in grid size
        if (self.__grid_size <= 2):
            return 0

        dif = grid_size - self.__grid_size
        half_dif = math.floor(dif / 2)

        if (dif == 0):
            return 0

        new_arr = np.zeros((grid_size, grid_size))

        # if new grid bigger add ald cells to the new array moved by a vector
        if (dif > 0):
            old_arr_shape = self.__cells.shape

            for x in range(old_arr_shape[0]):
                for y in range(old_arr_shape[1]):
                    if(self.__cells[y][x]):
                        new_arr[y + half_dif][x + half_dif] = True
                    else:
                        new_arr[y + half_dif][x + half_dif] = False

            self.__grid_size = grid_size
            self.__cells = new_arr

        elif (dif < 0):

            # new_arr_shape = new_arr.shape
            old_arr_shape = self.__cells.shape
            new_cells_list = []

            for x in range(old_arr_shape[0]):
                for y in range(old_arr_shape[1]):
                    if(self.__cells[y][x]):
                        new_cells_list.append((x + half_dif, y + half_dif))

            for cell in new_cells_list:
                new_arr[cell[1]][cell[0]] = True

            self.__grid_size = grid_size
            self.__cells = new_arr

    def Increment_grid_size(self):
        self.Set_grid_size(self.__grid_size + 2)

    def Decrement_grid_size(self):

        # checking if it would delete cells
        for i in range(self.__grid_size):
            if (self.__cells[i][0]):
                return False
            if (self.__cells[i][self.__grid_size - 1]):
                return False

        for i in range(self.__grid_size):
            if (self.__cells[0][i]):
                return False
            if (self.__cells[self.__grid_size - 1][i]):
                return False

        self.Set_grid_size(self.__grid_size - 2)
        return True

    def Draw(self):

        offset = self.__offset

        # calculating cell size
        rec_width = self.__screen.get_width() / self.__grid_size
        rec_height = self.__screen.get_height() / self.__grid_size

        # drawing alive cells
        for coord, cell in self.__alive_cells.items():
            rect = pygame.Rect(coord[0]*rec_width + offset[0], coord[1]*rec_height + offset[1], rec_width, rec_height)
            pygame.draw.rect(self.__screen, self.__alive_color, rect)

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
        # print("Time elapsed: ", t1, "  grid seize: ", self.__grid_size)
        return self.__grid_size

    def Step_back(self, num_of_steps):
        print("nothing")

    def Switch_cell(self, x, y):
        # check if out of boundries
        if (x < self.__grid_size and y < self.__grid_size):
            if(self.__cells[y][x] == True):
                self.__cells[y][x] = False
            else:
                self.__cells[y][x] = True

    def Turn_on_off_cell(self, x, y, on_off=True):
        # check if out of boundries
        if (x < self.__grid_size and y < self.__grid_size):
            if(on_off):
                self.__cells[y][x] = True
            else:
                self.__cells[y][x] = False

    def Get_grid_size(self):
        return self.__grid_size
