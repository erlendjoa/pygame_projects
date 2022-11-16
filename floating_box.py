import pygame
import os
from random import randint
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Floating Box")
FPS = 60

PLAYER_HIT = pygame.USEREVENT + 1

class Player():
    def __init__(self, health):
        self._health = health
        self._original_health = self._health
        self._moves = 2

    def move_1(self):
        self._move_1 = "Rock Smash"
        dmg = 15
        return dmg
    def move_2(self):
        self._move_2 = "Defense Curl"
        return "defense up"
    def get_moves(self):
        moves = []
        return moves

class Enemy():
    def __init__(self, health):
        self._health = health
        self._original_health = self._health

class Window():
    def __init__(self):
        self._player = Player(100)
        self._enemy = Enemy(80)

        self._BOX1 = pygame.Rect(150, HEIGHT//3, 100, 100)
        self._BOX2 = pygame.Rect(WIDTH-250, HEIGHT//3, 100, 100)
        self._FONT = pygame.font.SysFont("helvetica", 18)

        self._HEALTH_BAR_1 = pygame.Rect(self._BOX1.x-self._BOX1.width//5, self._BOX1.y+self._BOX1.height+40, 200, 20)
        self._HEALTH_BAR_2 = pygame.Rect(self._BOX2.x-self._BOX2.width//5, self._BOX2.y+self._BOX2.height+40, 200, 20)

        self._ACTION_BAR = pygame.Rect(WIDTH//2-250, HEIGHT*0.75, 500, 125)
        self._ACTION_MOVES = [pygame.Rect(self._ACTION_BAR.x+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+self._ACTION_BAR.width//2+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10*6, self._ACTION_BAR.width*0.42, 50), pygame.Rect(self._ACTION_BAR.x+self._ACTION_BAR.width//2+20, self._ACTION_BAR.y+self._ACTION_BAR.height//10*6, self._ACTION_BAR.width*0.42, 50)]

    def draw_window(self):
        WIN.fill((255, 255, 205))
        self.rectpros()
        self.blitpros()
        pygame.display.update()

    def rectpros(self):
        pygame.draw.rect(WIN, (0,255,0), self._BOX1)
        pygame.draw.rect(WIN, (0,0,255), self._BOX2)
        pygame.draw.rect(WIN, (255,0,0), self._HEALTH_BAR_1)
        pygame.draw.rect(WIN, (255,0,0), self._HEALTH_BAR_2)
        pygame.draw.rect(WIN, (0,0,0), self._ACTION_BAR)
        for i in range(self._player._moves):
            pygame.draw.rect(WIN, (255,255,255), self._ACTION_MOVES[i])
    def blitpros(self):
        self._FLOATING_TEXT1 = self._FONT.render("Player",1,(0,0,0))
        self._FLOATING_TEXT2 = self._FONT.render("Enemy",1,(0,0,0))
        self._PLAYER_HEALTH_TEXT = self._FONT.render(str(self._player._health),1,(255,255,255))
        self._ENEMY_HEALTH_TEXT = self._FONT.render(str(self._enemy._health),1,(255,255,255))
        WIN.blit(self._FLOATING_TEXT1, (self._BOX1.x, self._BOX1.y+self._BOX1.height+10))
        WIN.blit(self._FLOATING_TEXT2, (self._BOX2.x, self._BOX2.y+self._BOX2.height+10))
        WIN.blit(self._PLAYER_HEALTH_TEXT, (self._HEALTH_BAR_1.x+5, self._HEALTH_BAR_1.y))
        WIN.blit(self._ENEMY_HEALTH_TEXT, (self._HEALTH_BAR_2.x+5, self._HEALTH_BAR_2.y))

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
