import pygame

from pygame.sprite import *
class Joueur:
    def __init__(self, position_initiale, vitesse, saut):
        
        self.images_droite = [pygame.transform.scale(pygame.image.load("images/player_d.png"),(200,130)), pygame.transform.scale(pygame.image.load("images/player_dd.png"),(200,130))]
        self.images_gauche = [pygame.transform.scale(pygame.image.load("images/player_g.png"),(200,130)),pygame.transform.scale(pygame.image.load("images/player_gg.png"),(200,130))]
        self.images_repos = [pygame.transform.scale(pygame.image.load("images/player_face.png"),(200,130)),pygame.transform.scale(pygame.image.load("images/player_face_saut_1.png"),(200,130))]  # Ajoutez d'autres images si nécessaire
        self.vitesse_original = vitesse
        self.vitesse = vitesse
        self.saut = saut
        self.y_vitesse = 0
        self.on_ground = False
        self.live = 3
        self.score = 0
        self.position_initial = position_initiale[0] * 2
        self.moving = False
        self.current_images = self.images_repos
        self.current_image = 0
        self.image = self.current_images[self.current_image]
        self.rect = self.image.get_rect(midbottom=position_initiale)
        self.ecran_largeur = pygame.display.get_surface().get_width()
        
        
    def move_right(self):
        if self.rect.right < self.ecran_largeur  :
            self.vitesse = self.vitesse_original
            self.rect.x += self.vitesse  # Déplace le joueur vers la droite
            self.set_direction("droite")
            self.update_animation()
        

    def move_left(self):
        if self.rect.left >0:
            self.vitesse = self.vitesse_original
            self.rect.x -= self.vitesse  # Déplace le joueur vers la gauche
            self.set_direction("gauche")
            self.update_animation()
        
        
    def stop(self):
        self.vitesse = 0
        self.set_direction("stop")
        self.update_animation()
        


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_animation(self):
        self.current_image = (self.current_image + 1) % len(self.current_images)
        self.image = self.current_images[self.current_image]

    
    def set_idle(self):
        self.current_images = self.images_repos
        
    def set_direction(self, direction):
        if direction == "droite":
            self.current_images = self.images_droite
        elif direction == "gauche":
            self.current_images = self.images_gauche
        elif direction == "stop":
            self.current_images = self.images_repos
        # Réinitialiser l'index de l'image pour commencer l'animation de la nouvelle direction
        self.current_image = 0