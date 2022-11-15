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

PLAYER_HEALTH = 100
ENEMY_HEALTH = 50

BOX1 = pygame.Rect(150, HEIGHT//3, 100, 100)
BOX2 = pygame.Rect(WIDTH-250, HEIGHT//3, 100, 100)
FONT = pygame.font.SysFont("helvetica", 18)
FLOATING_TEXT1 = FONT.render("Player",1,(0,0,0))
FLOATING_TEXT2 = FONT.render("Enemy",1,(0,0,0))

HEALTH_BAR_1 = pygame.Rect(BOX1.x-BOX1.width//5, BOX1.y+BOX1.height+40, 200, 20)
HEALTH_BAR_2 = pygame.Rect(BOX2.x-BOX2.width//5, BOX2.y+BOX2.height+40, 200, 20)
PLAYER_HEALTH_TEXT = FONT.render(str(PLAYER_HEALTH),1,(255,255,255))
ENEMY_HEALTH_TEXT = FONT.render(str(ENEMY_HEALTH),1,(255,255,255))


def draw_window():
    WIN.fill((255, 255, 205))
    rectpros()
    blitpros()
    pygame.display.update()

def rectpros():
    pygame.draw.rect(WIN, (0,255,0), BOX1)
    pygame.draw.rect(WIN, (0,0,255), BOX2)
    pygame.draw.rect(WIN, (255,0,0), HEALTH_BAR_1)
    pygame.draw.rect(WIN, (255,0,0), HEALTH_BAR_2)
def blitpros():
    WIN.blit(FLOATING_TEXT1, (BOX1.x, BOX1.y+BOX1.height+10))
    WIN.blit(FLOATING_TEXT2, (BOX2.x, BOX2.y+BOX2.height+10))
    WIN.blit(PLAYER_HEALTH_TEXT, (HEALTH_BAR_1.x+5, HEALTH_BAR_1.y))
    WIN.blit(ENEMY_HEALTH_TEXT, (HEALTH_BAR_2.x+5, HEALTH_BAR_2.y))


def change_health(HEALTH):
        HEALTH -= 1
        print(HEALTH)

def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    pygame.event.post(pygame.event.Event(PLAYER_HIT))

            if event.type == PLAYER_HIT:
                change_health(PLAYER_HEALTH)
        
        if keys_pressed[pygame.K_5]:
            pygame.event.post(pygame.event.Event(PLAYER_HIT))

        draw_window()
    pygame.quit()
if __name__ == "__main__":
    main()