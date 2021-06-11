import pygame


class Background:
    def __init__(self, surface, display_size, grid_size, line_color, line_width):
        self.__screen = surface
        self.__display_size = display_size
        self.__grid_size = grid_size
        self.__line_color = line_color
        self.__line_width = line_width

        self.__offset = [0, 0]
        self.__zoom = 0

    def Set_grid_size(self, grid_size):
        self.__grid_size = grid_size
        self.Draw()

    def Draw(self):

        offset = self.__offset

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
        for i in range(len(offset)):
            self.__offset[i] += offset[i]
        self.Draw()
