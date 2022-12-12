import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Title of Game")
pygame.display.flip()


class Window():
    def __init__(self):
        pass


    def keys(self, keys_pressed):
        pass

    def event(self, event):
        pass

    def blit(self):
        pass

    def update(self):
        WIN.fill((255,255,255))
        pygame.display.update()

    def main(self):
        while True:
            pygame.time.Clock().tick(60)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.event(event)
            self.keys(keys_pressed)
            self.update()

Window().main()
