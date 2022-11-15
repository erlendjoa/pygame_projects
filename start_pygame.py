import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caption")
FPS = 60


#write global variables here...

def draw_window():
    WIN.fill((255, 225, 255))
    pygame.display.update()

#write functions here...


def main():
    run = True
    while run:
        pygame.time.Clock().tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.quit:
                run = False
            #write events here...

        #write something here...

        draw_window() 
    pygame.quit()
if __name__ == "__main__":
    main()