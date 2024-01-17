from pygame import *
from pygame.sprite import *
from .Objet import Objet
class ObjetSpeciaux(Objet):
    def __init__(self, position_initiale, vitesse):
        super().__init__("images\\triskel_droit.png", position_initiale, vitesse)
        self.son = pygame.mixer.Sound("sons\ponus.mp3")
    def action(self,joueur) :
        joueur.score += 20