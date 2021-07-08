import pygame
from game import Game
from controler import Controler

pygame.init()

game = Game((800, 800), 100, "Game of life by Martin Rybka")
mouse_keyboard = Controler(game)

pygame.font.init()

while True:
    mouse_keyboard.Event()
