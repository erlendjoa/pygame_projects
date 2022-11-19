import pygame
import os
from check import Colorcheck, Movecheck

COLORCHECK = Colorcheck()
MOVECHECK = Movecheck()

class Move():
    def __init__(self, name, type, dmg, val):
        self._name = name
        self._type = type
        self._color = COLORCHECK.get_color(type)
        self._dmg = dmg
        self._val = val
    
    def effectiveness(self, opponent):
        if MOVECHECK.check(self, opponent) == None:
            return self._dmg
        if MOVECHECK.check(self, opponent):
            return self._dmg + self._dmg//2
        if MOVECHECK.check(self, opponent) == False:
            return self._dmg - self._dmg//2
