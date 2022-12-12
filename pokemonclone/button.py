import pygame
import os

class Button():
    def __init__(self, main, pos, scale, color, text, elevation):
        self._main = main

        self._rect = pygame.Rect(pos, (scale[0], scale[1]))   #Rect style object
        self._bottom_rect = pygame.Rect(pos, (scale[0], elevation))
        _font = pygame.font.SysFont("Helvetica", 18)
        self._text_surface = _font.render(str(text),1,(0,0,0))
        self._text_rect = pygame.Rect(self._rect.x + self._rect.width//2 - 100//2, self._rect.y+5 + self._rect.height//8, 100, 50)
       
        self._color = color     #color code
        self._original_color = color    #original color code from init parameter
        self._dimmed_color = color    #darker color code for hovering

        if color[0] >= 25:
            self._dimmed_color = (self._dimmed_color[0]-25, self._dimmed_color[1], self._dimmed_color[2])
        if color[1] >= 25:
            self._dimmed_color = (self._dimmed_color[0], self._dimmed_color[1]-25, self._dimmed_color[2])
        if color[2] >= 25:
            self._dimmed_color = (self._dimmed_color[0], self._dimmed_color[1], self._dimmed_color[2]-25)

        self._elevation = elevation
        self._dynamic_elevation = elevation
        self._original_y = pos[1]

        self._original_text_y = pos[1]+5
        self._original_text2_y = pos[1]+25

        self._pressed = False
    
    def draw(self, WIN):
        self._rect.y = self._original_y - self._dynamic_elevation
        self._text_rect.y = self._original_text_y - self._dynamic_elevation
        pygame.draw.rect(WIN, self._color, self._rect)
        WIN.blit(self._text_surface, (self._text_rect))

    def action(self, action):
        self._main.battlewindow()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._color = self._dimmed_color
            if pygame.mouse.get_pressed()[0]:
                self._dynamic_elevation = 0
                self._pressed = True
            else:
                self._dynamic_elevation = self._elevation
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    self.action()
                    self._pressed = False
        else:
            self._dynamic_elevation = self._elevation
            self._color = self._original_color
    
    def simpleclick(self, bool):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._color = self._dimmed_color
            if pygame.mouse.get_pressed()[0]:
                self._dynamic_elevation = 0
                self._pressed = True
            else:
                self._dynamic_elevation = self._elevation
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    bool = True
                    self._pressed = False
        else:
            self._dynamic_elevation = self._elevation
            self._color = self._original_color


class ActionButton():
    def __init__(self, num, player, pos, width, height, color, text, elevation):
        self._num = num
        self._player = player

        self._rect = pygame.Rect(pos, (width, height))   #Rect style object
        self._bottom_rect = pygame.Rect(pos, (width, elevation))
        _font = pygame.font.SysFont("Helvetica", 18)
        self._text_surface = _font.render(str(text[0]),1,(0,0,0))
        self._text2_surface = _font.render(f"{text[1]} / {text[1]}",1,(0,0,0))
        self._text_rect = pygame.Rect(self._rect.x + self._rect.width//2 - 100//2, self._rect.y+5 + self._rect.height//8, 100, 50)
        self._text_rect2 = pygame.Rect(self._text_rect.x, self._text_rect.y+25, self._text_rect.width, self._text_rect.height)

        self._color = color     #color code
        self._original_color = color    #original color code from init parameter
        self._dimmed_color = color    #darker color code for hovering

        if color[0] >= 25:
            self._dimmed_color = (self._dimmed_color[0]-25, self._dimmed_color[1], self._dimmed_color[2])
        if color[1] >= 25:
            self._dimmed_color = (self._dimmed_color[0], self._dimmed_color[1]-25, self._dimmed_color[2])
        if color[2] >= 25:
            self._dimmed_color = (self._dimmed_color[0], self._dimmed_color[1], self._dimmed_color[2]-25)

        self._elevation = elevation
        self._dynamic_elevation = elevation
        self._original_y = pos[1]

        self._original_text_y = pos[1]+5
        self._original_text2_y = pos[1]+25

        self._pressed = False
    
    def draw(self, WIN):
        self._rect.y = self._original_y - self._dynamic_elevation
        self._text_rect.y = self._original_text_y - self._dynamic_elevation
        self._text_rect2.y = self._original_text2_y - self._dynamic_elevation
        pygame.draw.rect(WIN, self._color, self._rect)
        WIN.blit(self._text_surface, (self._text_rect))
        WIN.blit(self._text2_surface, (self._text_rect2))

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._color = self._dimmed_color
            if pygame.mouse.get_pressed()[0]:
                self._dynamic_elevation = 0
                self._pressed = True
            else:
                self._dynamic_elevation = self._elevation
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    self._player._usedmove = self._num
                    self._pressed = False
        else:
            self._dynamic_elevation = self._elevation
            self._color = self._original_color
    
    def simpleclick(self, bool):
        mouse_pos = pygame.mouse.get_pos()
        if self._rect.collidepoint(mouse_pos):
            self._color = self._dimmed_color
            if pygame.mouse.get_pressed()[0]:
                self._dynamic_elevation = 0
                self._pressed = True
            else:
                self._dynamic_elevation = self._elevation
                if self._pressed == True:
                    #<<< ON CLICK EVENTS >>>
                    bool = True
                    self._pressed = False
        else:
            self._dynamic_elevation = self._elevation
            self._color = self._original_color