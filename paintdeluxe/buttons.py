import pygame
import os


class ColorButton():
    def __init__(self, info, color):
        self._info = info
        self._color = color
        self._imgRect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])
        self._rect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])

        self._norScaled = (self._info[0], self._info[1], self._info[2], self._info[3])
        self._upScaled = (self._info[0]-3, self._info[1]-3, self._info[2]+6, self._info[3]+6)
        self._pressed = False

    def click(self, cursor):
            mouse_pos = pygame.mouse.get_pos()
            if self._rect.collidepoint(mouse_pos):
                self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._upScaled

                if pygame.mouse.get_pressed()[0]:
                    self._pressed = True

                else:
                    if self._pressed == True:
                        #<<< ON CLICK EVENTS >>>
                        cursor._wipe = False
                        cursor._rectColor = self._color

                        self._pressed = False
            else:
                self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._norScaled


    def blit(self, WIN, cursor):
        self.click(cursor)
        pygame.draw.rect(WIN, self._color, self._rect)
    

class SizeButton():
    def __init__(self, info, num):
        self._info = info
        self._num = num
        self._imgRect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])
        self._rect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])

        self._text = pygame.font.SysFont("comicsans", 20).render(str(num), 1, (0,0,0))

        self._norScaled = (self._info[0], self._info[1], self._info[2], self._info[3])
        self._upScaled = (self._info[0]-3, self._info[1]-3, self._info[2]+6, self._info[3]+6)
        self._pressed = False

    def click(self, cursor):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._upScaled

            if pygame.mouse.get_pressed()[0]:
                self._pressed = True

            else:
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    cursor._imgRect.width, cursor._imgRect.height = self._num*5,self._num*5

                    self._pressed = False
        else:
            self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._norScaled


    def blit(self, WIN, cursor):
        self.click(cursor)
        pygame.draw.rect(WIN, (90,90,90), self._rect)
        WIN.blit(self._text, (self._rect.x + self._rect.width//3, self._rect.y))


class EraseButton():
    def __init__(self, info, background):
        self._info = info
        self._background = background

        self._imgRect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])
        self._rect = pygame.Rect(self._info[0], self._info[1], self._info[2], self._info[3])
        self._text = pygame.font.SysFont("comicsans", 20).render("W", 1, (0,0,0))

        self._norScaled = (self._info[0], self._info[1], self._info[2], self._info[3])
        self._upScaled = (self._info[0]-3, self._info[1]-3, self._info[2]+6, self._info[3]+6)
        self._pressed = False

    def click(self, cursor):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._upScaled

            if pygame.mouse.get_pressed()[0]:
                self._pressed = True

            else:
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    cursor._wipe = True
                    cursor._rectColor = self._background.color

                    self._pressed = False
        else:
            self._rect.x, self._rect.y, self._rect.width, self._rect.height = self._norScaled

    def blit(self, WIN, cursor):
        self.click(cursor)
        pygame.draw.rect(WIN, (255,255,255), self._rect)
        WIN.blit(self._text, (self._rect.x + self._rect.width//10, self._rect.y))