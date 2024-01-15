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
    
      
    def draw_button(self,screen,background_color,text_color):
        x = self.x
        y = self.y
        width = self.height
        height = self.height
        text =self.text
        
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(screen, background_color, [x, y, width, height])
        text_render = font.render(text, True, text_color)
        screen.blit(text_render, (x + (width - text_render.get_width()) // 2, y + (height - text_render.get_height()) // 2))
    
    def is_clicked(self, x, y):
        # Vérifiez si les coordonnées x, y sont à l'intérieur des limites du bouton
        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y + self.height)