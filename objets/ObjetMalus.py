from pygame import *
from pygame.sprite import *
from .Objet import Objet
class ObjetMalus(Objet):
    def __init__(self, position_initiale, vitesse,niveau):
        self.niveau = niveau
        imagepath =self.choisir_image_en_fonction_du_niveau()
        
        super().__init__(imagepath, position_initiale, vitesse)
        
        self.son = pygame.mixer.Sound("sons\son_blessure_1.mp3")
    def action(self, joueur):
        joueur.live -= 1
    def choisir_image_en_fonction_du_niveau(self):
        if self.niveau == 1:
            return f"images\malus.png"
        elif self.niveau == 2:
            return f"images\cam_droit.png"
        # ... ajoutez autant de conditions que nécessaire ...
        elif self.niveau ==3 :
            return f"images\malus_normand.png"