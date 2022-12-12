import pygame
import os
from main_window import MainWindow
from battle_window import BattleWindow
from preset import Preset



class Main():
#startup object
    def __init__(self):
        self._mainwindow = MainWindow(self)
        self._battlewindow = BattleWindow(["pokemonclone","Assets","scenery.jpg"], Preset().get_Turtwig(True), Preset().get_Piplup(False))
        
        self.mainwindow()


    def mainwindow(self):
        run = True
        while run:
            pygame.time.Clock().tick(60)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    run = False
                self._mainwindow.eventpros(event)
            self._mainwindow.keys_pressed(keys_pressed)
            self._mainwindow.draw_window()
        pygame.quit()


    def battlewindow(self):
        run = True
        while run:
            pygame.time.Clock().tick(60)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    run = False
                self._battlewindow.eventpros(event)
            self._battlewindow.keys_pressed(keys_pressed)
            self._battlewindow.combatpros()
            self._battlewindow.draw_window()
        pygame.quit()

Main()