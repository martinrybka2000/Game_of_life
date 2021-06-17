
import numpy as np
import pygame
import math


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
        self.__cells = np.zeros((self.__number_of_steps, grid_size[0], grid_size[1]))
        self.__offset = [0, 0]
        self.__zoom = 0

        self.__cells[self.__actual_step][0][0] = True
        self.__cells[self.__actual_step][0][1] = True
        self.__cells[self.__actual_step][1][3] = True
        self.__cells[self.__actual_step][1][2] = True

    def __Judge_cell(self, x, y, step, neighbors):
        # rules of the game of life
        if (self.__cells[step][x][y] == True):
            if (neighbors < 2 or neighbors > 3):
                return False
            else:
                return True
        elif (neighbors == 3):
            return True

    def Set_grid_size(self, grid_size):
        # calculate the diference in grid size
        dif = [grid_size[0] - self.__grid_size[0], grid_size[1] - self.__grid_size[1]]
        self.__grid_size = grid_size

        if (dif[0] == 0 and dif[1] == 0):
            return 0

        new_arr = np.zeros((self.__number_of_steps, grid_size[0], grid_size[1]))

        # if new grid bigger add ald cells to the new array moved by a vector
        if (dif[0] > 0 and dif[1] > 0):
            old_arr_shape = self.__cells.shape

            for i in range(old_arr_shape[0]):
                for x in range(old_arr_shape[1]):
                    for y in range(old_arr_shape[2]):
                        if(self.__cells[i][x][y]):
                            new_arr[i][x + math.floor(dif[0] / 2)][y + math.floor(dif[1] / 2)] = True
                        else:
                            new_arr[i][x + math.floor(dif[0] / 2)][y + math.floor(dif[1] / 2)] = False

        self.__cells = new_arr

    def Increment_grid_size(self):
        self.Set_grid_size((self.__grid_size[0] + 2, self.__grid_size[1] + 2))

    def Draw(self):

        offset = self.__offset

        # list of alive cells
        alivecells = []

        # calculating cell size
        rec_width = self.__screen.get_width() / self.__grid_size[0]
        rec_height = self.__screen.get_height() / self.__grid_size[1]

        # looking for alive cells
        for x in range(self.__cells.shape[1]):
            for y in range(self.__cells.shape[2]):
                if (self.__cells[self.__actual_step][x][y] == True):
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
        for x in range(1, self.__cells.shape[1] - 1):
            for y in range(1, self.__cells.shape[2] - 1):

                neighbors = 0
                # if cell would count itself as her neighbor
                if (self.__cells[self.__actual_step][x][y] == True):
                    neighbors -= 1

                # count neighbors
                for i in range(9):
                    Vec_x = (i % 3) - 1
                    Vec_y = math.floor(i / 3) - 1
                    if (self.__cells[self.__actual_step][x + Vec_x][y + Vec_y] == True):
                        neighbors += 1

                # check if the cell dead or alive
                self.__cells[self.__actual_step + 1][x][y] = self.__Judge_cell(x, y, self.__actual_step, neighbors)

        self.__actual_step += 1

    def Step_back(self, num_of_steps):
        print("nothing")

    def Switch_cell(self, x, y):

        # check if out of boundries
        if (x < self.__grid_size[0] and y < self.__grid_size[1]):
            if(self.__cells[self.__actual_step][x][y] == True):
                self.__cells[self.__actual_step][x][y] = False
            else:
                self.__cells[self.__actual_step][x][y] = True
