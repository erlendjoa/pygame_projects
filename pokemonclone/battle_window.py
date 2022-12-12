import pygame
import os
from check import Colorcheck
from check import Movecheck
from preset import Preset
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Best Game Ever Made")
FPS = 60

PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2
MOVE_1 = pygame.USEREVENT + 3
CHANGE_CHAR1 = pygame.USEREVENT + 3
CHANGE_CHAR2 = pygame.USEREVENT + 4

class BattleWindow():
    def __init__(self, ref, player, enemy):
        self._ref = pygame.image.load(os.path.join(ref[0],ref[1],ref[2]))
        self._img = pygame.transform.rotate(pygame.transform.scale(self._ref, (WIDTH, HEIGHT)), 0)
        self._player = player
        self._enemy = enemy
        self._colorcheck = Colorcheck()
        self._preset = Preset()
        self._FONT = pygame.font.SysFont("Helvetica", 18)
        self._ACTION_BAR = pygame.Rect(WIDTH//2-250, HEIGHT*0.75, 400, 125)
        self._ACTION_MOVES = self._player.load_moves(self._ACTION_BAR)

    def draw_window(self):
        WIN.fill((208,218,220))
        self.rectpros()
        self.blitpros()
        pygame.display.update()

    def rectpros(self):
        pygame.draw.rect(WIN, (0,0,0), self._player._blackbar)
        pygame.draw.rect(WIN, (0,0,0), self._enemy._blackbar)
        pygame.draw.rect(WIN, (255,0,0), self._player._healthbar)
        pygame.draw.rect(WIN, (255,0,0), self._enemy._healthbar)
        self.draw_moves()
    def blitpros(self):
        self._FLOATING_TEXT1 = self._FONT.render(self._player._name,1,(0,0,0))
        self._FLOATING_TEXT2 = self._FONT.render(self._enemy._name,1,(0,0,0))
        self._PLAYER_HEALTH_TEXT = self._FONT.render(str(self._player._health),1,(255,255,255)) 
        self._ENEMY_HEALTH_TEXT = self._FONT.render(str(self._enemy._health),1,(255,255,255))
        WIN.blit(self._player._img, (self._player._sprite.x, self._player._sprite.y-50))
        WIN.blit(self._enemy._img, (self._enemy._sprite.x-50, self._enemy._sprite.y-50))
        WIN.blit(self._FLOATING_TEXT1, (self._player._healthbar.x, self._player._healthbar.y+self._player._healthbar.height+10))
        WIN.blit(self._FLOATING_TEXT2, (self._enemy._healthbar.x, self._enemy._healthbar.y+self._enemy._healthbar.height+10))
        WIN.blit(self._PLAYER_HEALTH_TEXT, (self._player._healthbar.x+5, self._player._healthbar.y))
        WIN.blit(self._ENEMY_HEALTH_TEXT, (self._enemy._healthbar.x+5, self._enemy._healthbar.y))
        
    def draw_moves(self):
        pygame.draw.rect(WIN, (165,184,187), self._ACTION_BAR)
        for i in range(len(self._player._moves)):
            self._player._ACTION_MOVES[i].click()
            self._player._ACTION_MOVES[i].draw(WIN)

    def combatpros(self):
        for i in range(len(self._player._moves)):
            if self._player._usedmove == i:
                print(f"{self._player._name} used {self._player._moves[i]._name}.")
                
                if self._player._moves[i].effectiveness(self._enemy) == None:
                    dmg_dealt = self._player._moves[i]._dmg

                if self._player._moves[i].effectiveness(self._enemy) == False:
                    print("Its not very effective...")
                    dmg_dealt = self._player._moves[i]._dmg//2

                if self._player._moves[i].effectiveness(self._enemy):
                    print("Its super effective!")
                    dmg_dealt = self._player._moves[i]._dmg + self._player._moves[i]._dmg//2

                pygame.event.post(pygame.event.Event(ENEMY_HIT))
                self._enemy._health -= dmg_dealt
                print(f"{self._enemy._name} took {dmg_dealt} damage!")

                self._player._usedmove = None

    def keys_pressed(self, keys_pressed):
        if keys_pressed[pygame.K_5]:
            pygame.event.post(pygame.event.Event(CHANGE_CHAR1))
        if keys_pressed[pygame.K_6]:
            pygame.event.post(pygame.event.Event(CHANGE_CHAR2))
        if keys_pressed[pygame.K_1]:
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
        if keys_pressed[pygame.K_2]:
            pygame.event.post(pygame.event.Event(ENEMY_HIT))

    def eventpros(self, event):
            if event.type == pygame.MOUSEBUTTONUP:
                pass
            if event.type == PLAYER_HIT:
                pass
            if event.type == ENEMY_HIT:
                pass
            if event.type == MOVE_1:
                pass
            if event.type == CHANGE_CHAR1:
                self._player = self._preset.get_Charmander(True)
                self._ACTION_MOVES = self._player.load_moves(self._ACTION_BAR)
            if event.type == CHANGE_CHAR2:
                self._player = self._preset.get_Piplup(True)
                self._ACTION_MOVES = self._player.load_moves(self._ACTION_BAR)