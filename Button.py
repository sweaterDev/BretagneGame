import pygame
import sys
from pygame.mixer import *
class Button():
    
    
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
    
      
    def draw_button(self,screen,text_color):
        x = self.x
        y = self.y
        width = self.height
        height = self.height
        text =self.text
        
        font = pygame.font.Font("eltirg__.ttf", 36)
        text_render = font.render(text, True, text_color)
        screen.blit(text_render, (x + (width - text_render.get_width()) // 2, y + (height - text_render.get_height()) // 2))
    
    def is_clicked(self,pos):
        # Vérifiez si les coordonnées x, y sont à l'intérieur des limites du bouton
        return self.rect.collidepoint(pos)