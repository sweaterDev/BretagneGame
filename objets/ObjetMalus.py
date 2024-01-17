from pygame import *
from pygame.sprite import *
from .Objet import Objet
class ObjetMalus(Objet):
    def __init__(self, position_initiale, vitesse):
        super().__init__("images\malus.png", position_initiale, vitesse)
        self.son = pygame.mixer.Sound("sons\son_blessure_1.mp3")
    def action(self, joueur):
        joueur.live -= 1   