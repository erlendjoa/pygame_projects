import pygame
import os

class Colorcheck():
    def __init__(self):
        pass
    def get_color(self, type):
        if type == "normal":
            return (169,169,169)
        elif type == "ground":
            return (200, 157, 124)
        elif type == "psychic":
            return (255, 142, 193)
        else:
            return (255,255,255)
