
import numpy as np
import pygame
import math
import random


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

        self.__cells = np.zeros((grid_size, grid_size))
        self.__offset = [0, 0]
        self.__zoom = 0

        for i in range(20):
            self.__cells[random.randint(0, grid_size - 1)][random.randint(0, grid_size - 1)] = True

        # self.__cells[0][1] = True
        # self.__cells[1][2] = True
        # self.__cells[2][0] = True
        # self.__cells[2][1] = True
        # self.__cells[2][2] = True

    def __Judge_cell(self, x, y, step, neighbors):
        # rules of the game of life
        if (self.__cells[y][x] == True):
            if (neighbors < 2 or neighbors > 3):
                return False
            else:
                return True
        elif (neighbors == 3):
            return True
        else:
            return False

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

        # print(self.__cells)
        # print("\n")

    def Increment_grid_size(self):
        self.Set_grid_size(self.__grid_size + 2)

    def Decrement_grid_size(self):

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

        # print(self.__cells)
        # print("\n")

        # list of alive cells
        alivecells = []

        # calculating cell size
        rec_width = self.__screen.get_width() / self.__grid_size
        rec_height = self.__screen.get_height() / self.__grid_size

        # looking for alive cells
        for x in range(self.__cells.shape[0]):
            for y in range(self.__cells.shape[1]):
                if (self.__cells[y][x] == True):
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

        # iterate thru the inner square
        self.Set_grid_size(self.__grid_size + 4)

        new_cells = np.zeros((self.__grid_size, self.__grid_size))

        for x in range(1, self.__cells.shape[0] - 1):
            for y in range(1, self.__cells.shape[1] - 1):

                neighbors = 0
                # if cell would count itself as her neighbor
                if (self.__cells[y][x] == True):
                    neighbors -= 1

                # count neighbors
                for i in range(9):
                    Vec_x = (i % 3) - 1
                    Vec_y = math.floor(i / 3) - 1
                    if (self.__cells[y + Vec_y][x + Vec_x] == True):
                        neighbors += 1

                # check if the cell dead or alive
                new_cells[y][x] = self.__Judge_cell(x, y, self.__actual_step, neighbors)

        self.__actual_step += 1
        self.__cells = new_cells
        for i in range(2):
            self.Decrement_grid_size()

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
