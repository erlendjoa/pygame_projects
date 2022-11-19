import pygame
import os
from color_class import Colorcheck

COLORCHECK = Colorcheck()

class Move():
    def __init__(self, name, type, dmg, val):
        self._name = name
        self._type = type
        self._color = COLORCHECK.get_color(type)
        self._dmg = dmg
        self._val = val
