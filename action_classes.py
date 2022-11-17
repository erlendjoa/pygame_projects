import pygame
import os

class Player():
    def __init__(self, name, health):
        self._ref = pygame.image.load(os.path.join("xprojekt1", "Assets", "po.webp"))
        self._img = pygame.transform.rotate(pygame.transform.scale(self._ref, (100, 150)), 0)
        self._name = name
        self._health = health
        self._original_health = self._health
        self._moves = [None, None, None, None]
    def set_move(self, name, type, dmg):
        for i in range(len(self._moves)):
            if self._moves[i] == None:
                self._moves[i] = str(name), str(type), int(dmg)
                break

class Enemy():
    def __init__(self, name, health):
        self._ref = pygame.image.load(os.path.join("xprojekt1", "Assets", "tai_lung.webp"))
        self._img = pygame.transform.rotate(pygame.transform.scale(self._ref, (150,150)), 0)
        self._name = name
        self._health = health
        self._original_health = self._health
