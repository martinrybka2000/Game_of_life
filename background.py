import pygame
import math


class Background:
    def __init__(self, surface, grid_size, line_color, line_width):
        self.__screen = surface
        self.__display_size = surface.get_size()
        self.__grid_size = grid_size
        self.__line_color = line_color
        self.__line_width = line_width

        self.__offset = [0, 0]
        self.__zoom = 0

    def Set_grid_size(self, grid_size):
        self.__grid_size = grid_size
        # self.Draw()

    def Increment_grid_size(self):
        self.Set_grid_size((self.__grid_size[0] + 2, self.__grid_size[1] + 2))

    def Decrement_grid_size(self):
        # if (self.__grid_size[0] - 2)
        self.Set_grid_size((self.__grid_size[0] - 2, self.__grid_size[1] - 2))

    def Draw(self):

        offset = [0, 0]

        # drawing nine square grids
        for i in range(9):
            Vec_x = (i % 3) - 1
            Vec_y = math.floor(i / 3) - 1

            offset[0] = self.__offset[0] + Vec_x*self.__display_size[0]
            offset[1] = self.__offset[1] + Vec_y*self.__display_size[1]

            # beginning positions for lines
            y0 = -1 + offset[1]
            y1 = self.__display_size[1] + 1 + offset[1]
            x0 = -1 + offset[0]
            x1 = self.__display_size[0] + 1 + offset[0]

            # calculating the distance between lines
            x_offset = self.__display_size[0] / (self.__grid_size[0])
            y_offset = self.__display_size[1] / (self.__grid_size[1])

            # drawing horisontal lines
            for i in range(self.__grid_size[0] + 1):
                pygame.draw.line(self.__screen, self.__line_color, (x_offset * i - 1 + offset[0], y0), (x_offset * i - 1 + offset[0], y1), self.__line_width)

            # drawing vertical lines
            for i in range(self.__grid_size[1] + 1):
                pygame.draw.line(self.__screen, self.__line_color, (x0, y_offset * i - 1 + offset[1]), (x1, y_offset * i - 1 + offset[1]), self.__line_width)

    # adding the offeset vector and Drawing the lines again
    def Move(self, offset):
        # adding the offset
        for i in range(len(offset)):
            self.__offset[i] += offset[i]

        # variables for looping the background
        off_x = self.__offset[0]
        off_y = self.__offset[1]

        width = self.__screen.get_width()
        height = self.__screen.get_height()

        looping_offset = [0, 0]

        # looping the background
        if (off_x > width):
            looping_offset[0] += (-width)

        elif (off_x < (-width)):
            looping_offset[0] += width

        elif (off_y > height):
            looping_offset[1] += (-height)

        elif (off_y < (-height)):
            looping_offset[1] += height

        for i in range(len(looping_offset)):
            self.__offset[i] += looping_offset[i]

        self.Draw()
