import pygame
import os

class Colorcheck():
    def __init__(self):
        pass
    def get_color(self, type):
        if type == "normal":
            return (169,169,169)
        elif type == "grass":
            return (144,238,144)
        elif type == "water":
            return (135,206,235)
        elif type == "fire":
            return (255,105,97)
        elif type == "ground":
            return (200, 157, 124)
        elif type == "psychic":
            return (255, 142, 193)
        elif type == "fighting":
            return (255, 127, 0)
        else:
            return (255,255,255)


class Movecheck():
    def __init__(self):
        self._normal = "normal"
        self._grass = "grass"
        self._water = "water"
        self._fire = "fire"
        self._ground = "ground"
        self._fighting = "fighting"
        self._psychic = "psychic"

    def check(self, move, opponent):    #Optimize with effective lists? For-loop?

        if (move._type == opponent._type) or (move._type == self._normal):
            return None

        if move._type == self._grass and opponent._type == self._fire:
            return False
        if move._type == self._water and opponent._type == self._grass:
            return False
        if move._type == self._fire and opponent._type == self._water:
            return False

        if move._type == self._grass and opponent._type == self._water:
            return True
        if move._type == self._water and opponent._type == self._fire:
            return True
        if move._type == self._fire and opponent._type == self._grass:
            return True
        
        return None