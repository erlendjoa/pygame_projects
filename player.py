import pygame
import os
from color_class import Colorcheck
from button import Button

colorcheck = Colorcheck()


class Player():
    def __init__(self, ref, side, name, health):
        self._ref = pygame.image.load(os.path.join(ref[0],ref[1],ref[2]))
        self._img = pygame.transform.rotate(pygame.transform.scale(self._ref, (100, 150)), 0)

        self._sprite = pygame.Rect(side[0])
        self._healthbar = pygame.Rect(side[1])
        self._healthtext = pygame.Rect(self._healthbar.x-self._healthbar.width//5, self._healthbar.y+self._healthbar.height+40, 200, 20)
        self._blackbar = pygame.Rect(self._healthbar.x, self._healthbar.y, self._healthbar.width, self._healthbar.height)

        self._name = name
        self._health = health
        self._original_health = self._health

        self._moves = []
        self._usedmove = None

    def load_moves(self, action_bar):
        self._ACTION_MOVES = []
        if len(self._moves) == 1:
            self._ACTION_MOVES.append(Button(0, self, (action_bar.x+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[0]._color, [self._moves[0]._name, self._moves[0]._val], 6))
        if len(self._moves) == 2:
            self._ACTION_MOVES.append(Button(0, self, (action_bar.x+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[0]._color, [self._moves[0]._name, self._moves[0]._val], 6))
            self._ACTION_MOVES.append(Button(1, self, (action_bar.x+action_bar.width//2+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[1]._color, [self._moves[1]._name, self._moves[1]._val], 6))
        if len(self._moves) == 3:
            self._ACTION_MOVES.append(Button(0, self, (action_bar.x+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[0]._color, [self._moves[0]._name, self._moves[0]._val], 6))
            self._ACTION_MOVES.append(Button(1, self, (action_bar.x+action_bar.width//2+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[1]._color, [self._moves[1]._name, self._moves[1]._val], 6))
            self._ACTION_MOVES.append(Button(2, self, (action_bar.x+20, action_bar.y+action_bar.height//10*6), action_bar.width*0.42, 50, self._moves[2]._color, [self._moves[2]._name, self._moves[2]._val], 6))
        if len(self._moves) == 4: 
            self._ACTION_MOVES.append(Button(0, self, (action_bar.x+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[0]._color, [self._moves[0]._name, self._moves[0]._val], 6))
            self._ACTION_MOVES.append(Button(1, self, (action_bar.x+action_bar.width//2+20, action_bar.y+action_bar.height//10), action_bar.width*0.42, 50, self._moves[1]._color, [self._moves[1]._name, self._moves[1]._val], 6))
            self._ACTION_MOVES.append(Button(2, self, (action_bar.x+20, action_bar.y+action_bar.height//10*6), action_bar.width*0.42, 50, self._moves[2]._color, [self._moves[2]._name, self._moves[2]._val], 6))
            self._ACTION_MOVES.append(Button(3, self, (action_bar.x+action_bar.width//2+20, action_bar.y+action_bar.height//10*6), action_bar.width*0.42, 50, self._moves[3]._color, [self._moves[3]._name, self._moves[3]._val], 6))

    def set_move(self, move):
        self._moves.append(move)

    def use_move(self, num):
            print(f"{self._name} used {self._moves[num]._name}!")
            self._usedmove = num

class Enemy():
    def __init__(self, ref, name, health):
        self._ref = pygame.image.load(os.path.join(ref[0],ref[1],ref[2]))
        self._img = pygame.transform.rotate(pygame.transform.scale(self._ref, (150,150)), 0)

        self._sprite = pygame.Rect(900-250, 500//3, 200, 100)
        self._healthbar = pygame.Rect(900-250, 500//3+120, 200, 20)    #1. argument er WIDTH aka 900. 2. arument er HEIGHT aka 500.
        self._healthtext = self._healthbar.x-self._healthbar.width//5, self._healthbar.y+self._healthbar.height+40, 200, 20
        self._blackbar = pygame.Rect(self._healthbar.x, self._healthbar.y, self._healthbar.width, self._healthbar.height)

        self._name = name
        self._health = health
        self._original_health = self._health
        self._moves = [None, None, None, None]

    def set_move(self, name, type, dmg, val):
        for i in range(len(self._moves)):
            if self._moves[i] == None:
                self._moves[i] = str(name), str(type), int(dmg), int(val)
                break
    def use_move(self):
        pass
