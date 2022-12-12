import pygame
import os

from window import Window

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Deluxe")
pygame.display.flip()


class Main():
    def __init__(self):
        self._window = Window(Background)


    def keys(self, keys_pressed):
        if keys_pressed[pygame.K_5]:
            Background.color = (255,105,86)
            self._window._cursor._rectColor = Background.color
            for rect in self._window._drawRects:
                if rect._check == True:
                    rect._color = Background.color

        if keys_pressed[pygame.K_4]:
            Background.color = (255,255,255)
            self._window._cursor._rectColor = Background.color
            for rect in self._window._drawRects:
                if rect._check == True:
                    rect._color = Background.color

    def event(self, event):
        pass

    def blit(self):
        self._window.blit(WIN)

    def update(self):
        WIN.fill((255,255,255))
        self.blit()
        pygame.display.update()

    def main(self):
        while True:
            pygame.time.Clock().tick(270)
            keys_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                self.event(event)
            self.keys(keys_pressed)
            self.update()

class Background():
    color = (255,255,255)

    def __init__(self):
        pass


Main().main()