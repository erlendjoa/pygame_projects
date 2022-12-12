import pygame
import os

from buttons import ColorButton, SizeButton, EraseButton
from cursor import Cursor

WIDTH, HEIGHT = 900, 500

class Window():
    def __init__(self, background):
        self._background = background

        self._topBorder = pygame.Rect(50,0, WIDTH,50)
        self._leftBorder = pygame.Rect(0,0, 50,HEIGHT)
        self._window = pygame.Rect(50,50, WIDTH, HEIGHT)

        self._drawRects = []

        self._buttons = []
        for rgb in range(0,253):
            self._button = ColorButton([self._topBorder.x+rgb, self._topBorder.y+10, 1,40], (rgb,rgb+1,rgb+2))
            self._buttons.append(self._button)
 
            

        self._button1 = ColorButton([self._topBorder.x, self._topBorder.y, 60,10], (0,255,0))
        self._button2 = ColorButton([self._topBorder.x+60, self._topBorder.y, 60,10], (255,0,0))
        self._button3 = ColorButton([self._topBorder.x+120, self._topBorder.y, 60,10], (0,0,255))
        self._button4 = ColorButton([self._topBorder.x+180, self._topBorder.y, 60,10], (255,255,255))
        self._buttons.append(self._button1)
        self._buttons.append(self._button2)
        self._buttons.append(self._button3)
        self._buttons.append(self._button4)
        
            
        self._button01 = SizeButton([10, self._topBorder.height+10, 30,30], 1)
        self._button02 = SizeButton([10, self._topBorder.height+50, 30,30], 2)
        self._button03 = SizeButton([10, self._topBorder.height+90, 30,30], 3)
        self._buttonE = EraseButton([10, 10, 30,30], self._background)
        self._buttons.append(self._button01)
        self._buttons.append(self._button02)
        self._buttons.append(self._button03)
        self._buttons.append(self._buttonE)

        self._cursor = Cursor((0,0,0))

        self._pressed = False
    
    def click(self):
                mouse_pos = pygame.mouse.get_pos()
                if self._window.collidepoint(mouse_pos):
                    pass

                    if pygame.mouse.get_pressed()[0]:
                        self._pressed = True
                        if self._cursor._wipe == True:
                            self._drawRects.append(Drawing([mouse_pos[0], mouse_pos[1], self._cursor._imgRect.width, self._cursor._imgRect.height], (self._cursor._rectColor), True))
                        else:
                            self._drawRects.append(Drawing([mouse_pos[0], mouse_pos[1], self._cursor._imgRect.width, self._cursor._imgRect.height], (self._cursor._rectColor), False))

                    else:
                        if self._pressed == True:
                            #<<< ON CLICK EVENTS >>>

                            self._pressed = False
                else:
                    pass


    def blit(self, WIN):
        self.click()
        pygame.draw.rect(WIN, self._background.color, self._window)
        pygame.draw.rect(WIN, (155,155,155), self._topBorder)
        pygame.draw.rect(WIN, (105,105,105), self._leftBorder)

        for button in self._buttons:
            button.blit(WIN, self._cursor)

        for rect in self._drawRects:
            rect.blit(WIN)

        self._cursor.blit(WIN)



class Drawing():
    def __init__(self, info, color, boolean):
        self._rect = pygame.Rect(info[0],info[1], info[2],info[3])
        self._color = color
        
        self._check = None
        if boolean == True:
            self._check = True
        elif boolean == False:
            self._check = False
    
    def blit(self, WIN):
        pygame.draw.rect(WIN, self._color, self._rect)