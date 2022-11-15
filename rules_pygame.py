import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caption")
FPS = 60

EVENT1 = pygame.USEREVENT + 1   #lager en event med 1 som referanse.
RGB = (255, 255, 255)
IMGREF = pygame.image.load(os.path.join("Mappe", "Assets", "bilde.png"))   #filreferanse
IMG = pygame.transform.rotate(pygame.transform.scale(IMGREF, (200, 400)), 90)   #(referanse, (bredde, høyde), rotasjon)
RECT = pygame.Rect(0, 0, 200, 400)  #x, y, bredde, høyde  
FONT = pygame.font.SysFont("comicsans", 40)  #tekstfont, størrelse
SOUND = pygame.mixer.Sound(os.path.join("Mappe", "Assets", "sang.wav"))    #filreferanse



def draw_window():
    WIN.fill((RGB))

    WIN.blit(IMG, (0, 0))  #blit() plasserer referanse på skjermen med top/left som startsposisjon i img.
    pygame.draw.rect(WIN, RGB, RECT)    #tegner element med argumet: (WIN, RGB, Rect).

    TEXT = FONT.render("Text", 1, RGB) #definerer tekst med .render, bruk alltid 1 som tredje argument.
    WIN.blit(TEXT, (0, 0))

    SOUND.play()    #spiller av lydspor.

    pygame.time.delay(5000) #skaper et i dette tilfellet 5 sek delay.
    
    pygame.display.update() #skjerm oppdateres



def main():
    run = True
    while run:  #spill-loop. kjører hver gang run == True
        pygame.time.Clock().tick(FPS)   #oppdaterer frame, styrer at den ikke går over FPS cap.
        keys_pressed = pygame.key.get_pressed() #sjekker alle keys og refererer til den key som blir presset.
        for event in pygame.event.get():
            if event.type == pygame.quit:   #sjekker om quit.
                run = False
            
            if event.type == pygame.KEYDOWN:    #sjekker keys presset.
                if event.key == pygame.K_a:
                    pass

            if event.type == EVENT1:    #If event skjer: 
                pass

        draw_window() 
    pygame.quit()
if __name__ == "__main__":
    main()