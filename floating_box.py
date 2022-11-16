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

    def get_health(self):
        return self._health
    
    def change_health(self, damage):
        while self._health > self._original_health - damage:
            self._health -= 1
            pygame.time.delay(50)
        self._original_health = self._health
        return self._health


class Enemy():
    def __init__(self, health):
        self._health = health
    def create_font(self, font):
        ENEMY_HEALTH_TEXT = font.render(str(self._health),1,(255,255,255))
        return ENEMY_HEALTH_TEXT
    def create_rect(self, rect):
        HEALTH_BAR_2 = pygame.Rect(rect.x-rect.width//5, rect.y+rect.height+40, 200, 20)
        return HEALTH_BAR_2



class Window():
    def __init__(self):
        self._player = Player(100)
        self._enemy = Enemy(80)

        self._BOX1 = pygame.Rect(150, HEIGHT//3, 100, 100)
        self._BOX2 = pygame.Rect(WIDTH-250, HEIGHT//3, 100, 100)
        self._FONT = pygame.font.SysFont("helvetica", 18)

        self._FLOATING_TEXT1 = self._FONT.render("Player",1,(0,0,0))
        self._FLOATING_TEXT2 = self._FONT.render("Enemy",1,(0,0,0))
        self._PLAYER_HEALTH_TEXT = self._FONT.render(str(self._player._health),1,(255,255,255))
        self._ENEMY_HEALTH_TEXT = self._FONT.render(str(self._enemy._health),1,(255,255,255))
        self._HEALTH_BAR_1 = pygame.Rect(self._BOX1.x-self._BOX1.width//5, self._BOX1.y+self._BOX1.height+40, 200, 20)
        self._HEALTH_BAR_2 = pygame.Rect(self._BOX2.x-self._BOX2.width//5, self._BOX2.y+self._BOX2.height+40, 200, 20)

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
    def blitpros(self):
        WIN.blit(self._FLOATING_TEXT1, (self._BOX1.x, self._BOX1.y+self._BOX1.height+10))
        WIN.blit(self._FLOATING_TEXT2, (self._BOX2.x, self._BOX2.y+self._BOX2.height+10))
        WIN.blit(self._PLAYER_HEALTH_TEXT, (self._HEALTH_BAR_1.x+5, self._HEALTH_BAR_1.y))
        WIN.blit(self._ENEMY_HEALTH_TEXT, (self._HEALTH_BAR_2.x+5, self._HEALTH_BAR_2.y))

    def keys_pressed(self, keys_pressed):
        if keys_pressed[pygame.K_5]:
            pygame.event.post(pygame.event.Event(PLAYER_HIT))

    def main(self):
        run = True
        while run:
            pygame.time.Clock().tick(FPS)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL:
                        pass
                if event.type == PLAYER_HIT:
                    self._player._health = self._player.change_health(10)

            self.keys_pressed(keys_pressed)
            self.draw_window()

        pygame.quit()
win = Window()
win.main()
