import pygame
import os
from random import randint
from button import Button

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")
FPS = 60


class MainWindow():
    def __init__(self, main):
        self._main = main
        self._button_1 = Button(self._main, (WIDTH//2-50, HEIGHT//2-25), [100, 50], (255,255,255), "Start", 6)
        

    def draw_window(self):
        WIN.fill((144,238,144))
        self.rectpros()
        self.blitpros()
        pygame.display.update()

    def rectpros(self):
        pass    
    def blitpros(self):
        self._button_1.draw(WIN)
        if self._button_1.simpleclick(False):
            print("hei")
    def keys_pressed(self, keys_pressed):
        if keys_pressed[pygame.K_ESCAPE]:
            self._main.battlewindow()
    def eventpros(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pass
    