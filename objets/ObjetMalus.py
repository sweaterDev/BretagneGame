from pygame import *
from pygame.sprite import *
from Objet import Objet
class ObjetMalus(Objet):
    def __init__(self):  
        Objet.__init__(self)
        self.image = image.load("filename").convert()
       