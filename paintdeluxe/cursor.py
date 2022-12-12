import pygame
import os

class Cursor():
    def __init__(self, rectColor):
        self._imgRect = pygame.Rect(0,0,10,10)
        self._rectColor = rectColor
        
        self._colorcheck = "white"
        self._wipe = False


    def mouse(self):
        pos = pygame.mouse.get_pos()
        self._imgRect.x = pos[0] - self._imgRect.width//2
        self._imgRect.y = pos[1] - self._imgRect.height//2

    def blit(self, WIN):
        self.mouse()
        pygame.draw.rect(WIN, self._rectColor, self._imgRect)