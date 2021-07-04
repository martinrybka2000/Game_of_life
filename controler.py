
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
        self.__mouse_draging = False

    def Event(self):

        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        mouse_keys = pygame.mouse.get_pressed()

        # event handling
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONUP:
                if mouse_keys[0]:
                    if (self.__mouse_down and not self.__mouse_moving):
                        self.__game.Click(self.__mouse_pos[0], self.__mouse_pos[1])

                self.__mouse_down = False
                self.__mouse_moving = False
                self.__mouse_draging = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__mouse_pos = pygame.mouse.get_pos()
                self.__mouse_down = True
                self.__mouse_moving = False

                if event.button == 4:
                    self.__game.Zoom(-10)
                if event.button == 5:
                    self.__game.Zoom(10)

            if event.type == pygame.MOUSEMOTION:
                self.__mouse_moving = True
                if(self.__mouse_down):
                    if (mods & pygame.KMOD_LCTRL):
                        if (self.__mouse_draging):
                            self.__game.Move(pygame.mouse.get_rel())
                        else:
                            pygame.mouse.get_rel()
                            self.__mouse_draging = True

                    elif(mods & pygame.KMOD_LSHIFT):
                        pos = pygame.mouse.get_pos()
                        self.__game.Click(pos[0], pos[1], True, pygame.KMOD_LSHIFT)
                        self.__mouse_draging = False
                    else:
                        pos = pygame.mouse.get_pos()
                        self.__game.Click(pos[0], pos[1], True)
                        self.__mouse_draging = False

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

        elif keys[pygame.K_SPACE]:
            self.__game.Tick()

        elif keys[pygame.K_n] and self.__button_flag:
            self.__button_flag = False

        elif keys[pygame.K_n] == False and self.__button_flag == False:
            self.__game.Tick()
            self.__button_flag = True

        # delay
        pygame.time.delay(5)
