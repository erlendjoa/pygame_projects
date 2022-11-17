import pygame
import os
from random import randint
from color_class import Colorcheck
from action_classes import Player
from action_classes import Enemy

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floating Box")
FPS = 60

PLAYER_HIT = pygame.USEREVENT + 1

class Window():
    def __init__(self):
        self._colorcheck = Colorcheck()
        self._player = Player("Po", 100)
        self._player.set_move("Rock Smash", "ground", 25)
        self._player.set_move("Psychic Beam", "psychic", 35)
        self._enemy = Enemy("Tai Lung", 80)

        self._BOX1 = pygame.Rect(100, HEIGHT//3, 200, 100)
        self._BOX2 = pygame.Rect(WIDTH-250, HEIGHT//3, 200, 100)
        self._FONT = pygame.font.SysFont("helvetica", 18)

        self._HEALTH_BAR_1 = pygame.Rect(self._BOX1.x-self._BOX1.width//5, self._BOX1.y+self._BOX1.height+40, 200, 20)
        self._HEALTH_BAR_2 = pygame.Rect(self._BOX2.x-self._BOX2.width//5, self._BOX2.y+self._BOX2.height+40, 200, 20)

        self._ACTION_BAR = pygame.Rect(WIDTH//2-250, HEIGHT*0.75, 500, 125)
        self._ACTION_MOVES = [pygame.Rect(self._ACTION_BAR.x+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+self._ACTION_BAR.width//2+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10*6, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+self._ACTION_BAR.width//2+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10*6, self._ACTION_BAR.width*0.42, 50)]

    def draw_window(self):
        WIN.fill((220,220,220))
        self.rectpros()
        self.blitpros()
        pygame.display.update()

    def rectpros(self):
        pygame.draw.rect(WIN, (255,0,0), self._HEALTH_BAR_1)
        pygame.draw.rect(WIN, (255,0,0), self._HEALTH_BAR_2)
        self.draw_moves()
    def blitpros(self):
        self._FLOATING_TEXT1 = self._FONT.render(self._player._name,1,(0,0,0))
        self._FLOATING_TEXT2 = self._FONT.render(self._enemy._name,1,(0,0,0))
        self._PLAYER_HEALTH_TEXT = self._FONT.render(str(self._player._health),1,(255,255,255))
        self._ENEMY_HEALTH_TEXT = self._FONT.render(str(self._enemy._health),1,(255,255,255))
        WIN.blit(self._player._img, (self._BOX1.x, self._BOX1.y-50))
        WIN.blit(self._enemy._img, (self._BOX2.x-50, self._BOX2.y-50))
        WIN.blit(self._FLOATING_TEXT1, (self._BOX1.x, self._BOX1.y+self._BOX1.height+10))
        WIN.blit(self._FLOATING_TEXT2, (self._BOX2.x, self._BOX2.y+self._BOX2.height+10))
        WIN.blit(self._PLAYER_HEALTH_TEXT, (self._HEALTH_BAR_1.x+5, self._HEALTH_BAR_1.y))
        WIN.blit(self._ENEMY_HEALTH_TEXT, (self._HEALTH_BAR_2.x+5, self._HEALTH_BAR_2.y))
    def draw_moves(self):
        pygame.draw.rect(WIN, (0,0,0), self._ACTION_BAR)
        for i in range(len(self._player._moves)):
            if self._player._moves[i] != None:
                pygame.draw.rect(WIN, self._colorcheck.get_color(self._player._moves[i][1]), self._ACTION_MOVES[i])
                text = self._FONT.render(str(self._player._moves[i][0]),1,(0,0,0))
                WIN.blit(text, (self._ACTION_MOVES[i].x, self._ACTION_MOVES[i].y))

    def keys_pressed(self, keys_pressed):
        if keys_pressed[pygame.K_5]:
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
    def eventpros(self, event):
            if event.type == PLAYER_HIT:
                self._player._health -= self._enemy.move_1()
                if self._player._health > 0:
                    self._HEALTH_BAR_1.width -= self._HEALTH_BAR_1.width//self._player._health*self._enemy.move_1()
        

    def main(self):
        run = True
        while run:
            pygame.time.Clock().tick(FPS)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    return False
                self.eventpros(event)

            self.keys_pressed(keys_pressed)

            self.draw_window()
        pygame.quit()
win = Window()
win.main()
