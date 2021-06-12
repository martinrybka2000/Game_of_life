

class Cells:
    def __init__(self, display_size, grid_size, back_color, alive_color, line_width):
        self.__display_size = display_size
        self.__grid_size = grid_size
        self.__back_color = back_color
        self.__alive_color = alive_color
        self.__line_width = line_width

        number_of_steps = 10

        self.__cells = [grid_size[0], grid_size[1], number_of_steps]
        self.__offset = [0, 0]
        self.__zoom = 0

    def Set_grid_size(self, grid_size):
        self.__grid_size = grid_size

    def Draw(self):
        print("nothing")

    def Move(self, offset):
        print("nothing")

    def Step_up(self, num_of_steps):
        print("nothing")

    def Step_back(self, num_of_steps):
        print("nothing")

    def Switch_cell(self, xy):
        print("nothing")
