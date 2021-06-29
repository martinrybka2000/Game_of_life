import pygame
# import numpy as np
from game import Game
from controler import Controler

pygame.init()

# image = pygame.Surface([20, 20]).convert_alpha()

game = Game((800, 800), 100, "Game of life")
mouse_keyboard = Controler(game)

pygame.key.set_repeat(500, 20)

while True:
    mouse_keyboard.Event()
