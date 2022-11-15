import pygame
import os
pygame.font.init()  #initialiserer pygame sine tekstfonter.
pygame.mixer.init() #initialiserer lyd

pygame.display.set_caption("First Game")
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
VELOCITY = 5
BULLET_VELOCITY = 8
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
SPACESHIP_SCALE = SPACESHIP_WIDTH, SPACESHIP_HEIGHT
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)  #definerer hvilken tekstfont og størrelse.
WINNER_FONT = pygame.font.SysFont("comicsans", 100)
BUTLLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("pygameprosjekt", "Assets", "Aperture Science.wav"))    #definerer hvilken mp3 fil.

YELLOW_HIT = pygame.USEREVENT + 1   #lager en event med 1 som referanse.
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("pygameprosjekt", "Assets", "spaceship_yellow.png"))
#^referanse til .png i mappe.
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SCALE), 90)
#^referanse til transformere scalen/size og rotate til img.
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("pygameprosjekt", "Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SPACESHIP_SCALE), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("pygameprosjekt", "Assets", "space.png")),(WIDTH, HEIGHT))


def draw_window(yellow, red, bullets, health):
    WIN.fill(WHITE) #fyller vindu til RGB.
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)    #tegner element med argumet: (WIN, RGB, Rect).
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))  #blit() plasserer referanse på skjermen med top/left som startsposisjon i img.
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    red_health_text = HEALTH_FONT.render("Heatlh: " + str(health[0]), 1, WHITE) #definerer tekst med .render, bruk alltid 1 som tredje argument.
    yellow_health_text = HEALTH_FONT.render("Heatlh: " + str(health[1]), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, HEIGHT - red_health_text.get_height() - 10))
    WIN.blit(yellow_health_text, (10, HEIGHT - yellow_health_text.get_height() - 10))
    for b in bullets[0]:
        pygame.draw.rect(WIN, RED, b)
    for b in bullets[1]:
        pygame.draw.rect(WIN, YELLOW, b)
    pygame.display.update() #oppdaterer skjermen (FPS). Må alltid være med etter blit() prosedyrer.

def draw_winner(text):
    winner_font = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(winner_font, (WIDTH//2 - winner_font.get_width()//2, HEIGHT//2 - winner_font.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000) #skaper et i dette tilfellet 5 sek delay.

def yellow_handle_movement(keys_pressed, yellow):   #parameter er presset tast og rect.
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:    #hvis tast erlik "a"... and x pos - hastighet>kanten.
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < BORDER.x:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT:
        yellow.y += VELOCITY
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x + BORDER.width:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT:
        red.y += VELOCITY

def handle_bullets(bullets, yellow, red):
    for b in bullets[0]:
        b.x += BULLET_VELOCITY
        if red.colliderect(b):   #sjekk for kollisjon mellom Rect.
            pygame.event.post(pygame.event.Event(RED_HIT))  #lager ny event som sier at i dette tilfellet det skjedde en kollisjon.
            bullets[0].remove(b)
        elif b.x > WIDTH:
            bullets[0].remove(b)
    for b in bullets[1]:
        b.x -= BULLET_VELOCITY
        if yellow.colliderect(b):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            bullets[1].remove(b)
        elif b.x < 0:
            bullets[1].remove(b)


def main():
    yellow_Rect = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red_Rect = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    #^lager rektangel for hvert element med x,y posisjon og width, height størrelse.
    bullets = [[],[]]
    health = [5,5]

    run = True
    while run:  #spill-loop. kjører hver gang run != True
        pygame.time.Clock().tick(FPS)   #oppdaterer frame, styrer at den ikke går over FPS cap.
        keys_pressed = pygame.key.get_pressed() #sjekker alle keys og refererer til den key som blir presset.
        for event in pygame.event.get():    #sjekker om quit.
            if event.type == pygame.quit:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(bullets[0]) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow_Rect.x + yellow_Rect.width, yellow_Rect.y + yellow_Rect.height//2, 10, 5)
                    bullets[0].append(bullet)
                if event.key == pygame.K_RCTRL and len(bullets[1]) < MAX_BULLETS:
                    bullet = pygame.Rect(red_Rect.x, red_Rect.y + red_Rect.height//2, 10, 5)
                    bullets[1].append(bullet)

            if event.type == RED_HIT:
                health[0] -= 1
                BUTLLET_HIT_SOUND.play()    #starter lydspor.
            if event.type == YELLOW_HIT:
                health[1] -= 1
                BUTLLET_HIT_SOUND.play()

        winner_text = ""
        if health[1] <= 0:
            winner_text = "Red Wins!"
        if health[0] <= 0:
            winner_text = "Yellow Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            run = False
        yellow_handle_movement(keys_pressed, yellow_Rect)
        red_handle_movement(keys_pressed, red_Rect)
        handle_bullets(bullets, yellow_Rect, red_Rect)
        draw_window(yellow_Rect, red_Rect, bullets, health) #siste prosedyre!
    main()
main()