
import pygame
from game import Game


class Controler:
    def __init__(self, game):
        self.__game = game
        self.__button_flag = True
        self.__button_flag2 = True

        self.__mouse_pos = (0, 0)

        self.__mouse_down = False
        self.__mouse_moving = False

    def Event(self):

        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()

        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                if (self.__mouse_down and not self.__mouse_moving):
                    self.__game.Click(self.__mouse_pos[0], self.__mouse_pos[1])

                self.__mouse_down = False
                self.__mouse_moving = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_pos = pygame.mouse.get_pos()
                self.__mouse_down = True
                self.__mouse_moving = False

            if event.type == pygame.MOUSEMOTION:
                self.__mouse_moving = True
                if(self.__mouse_down):
                    if(mods & pygame.KMOD_LSHIFT):
                        pos = pygame.mouse.get_pos()
                        self.__game.Click(pos[0], pos[1], True, pygame.KMOD_LSHIFT)
                    else:
                        pos = pygame.mouse.get_pos()
                        self.__game.Click(pos[0], pos[1], True)

        # keys presing handling
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.__game.Move((10, 0))

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.__game.Move((-10, 0))

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.__game.Move((0, 10))

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.__game.Move((0, -10))

        elif keys[pygame.K_q]:
            self.__game.Zoom(1)

        elif keys[pygame.K_e]:
            self.__game.Zoom(-1)

        elif keys[pygame.K_SPACE] and self.__button_flag:
            self.__game.Tick()
            # self.__button_flag = False

        elif keys[pygame.K_SPACE] == False and self.__button_flag == False:
            self.__button_flag = True

        # delay
        pygame.time.delay(5)
