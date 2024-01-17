from pygame import *
from pygame.sprite import *
from .Objet import Objet

class ObjetBonus(Objet):
    def __init__(self, position_initiale, vitesse):
        self.images = [pygame.image.load(f"chouchen/frame-{i}.png") for i in range(1, 50)]
        super().__init__(self.images[0], position_initiale, vitesse)
        self.son = pygame.mixer.Sound("sons/ponus.mp3")
        self.current_image = 0
        self.animation_time = 115  # Temps en millisecondes pour changer d'image
        self.last_update = pygame.time.get_ticks()
    def update(self):
        super().update()
        
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_time:
            self.last_update = now
            self.current_image = (self.current_image + 1) % len(self.images)
            self.image = self.images[self.current_image]
        
    def action(self, joueur):
        joueur.score += 10
        