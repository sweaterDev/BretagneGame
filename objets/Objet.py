import pygame
from pygame.sprite import *
class Objet:
    
    def __init__(self, image_path, position_initiale, vitesse):
        if isinstance(image_path, str): 
            self.image = pygame.transform.scale(pygame.image.load(image_path), (170, 170))
        else :
            self.image = pygame.transform.scale(image_path, (170, 170))
        self.rect = self.image.get_rect(midtop=position_initiale)
        self.vitesse = vitesse

    def update(self):
        self.rect.y += self.vitesse

    def draw(self, screen):
        screen.blit(self.image, self.rect)