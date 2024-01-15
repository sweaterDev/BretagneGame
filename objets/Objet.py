from pygame import *
from pygame.sprite import *
class Objet(Sprite):
    def __init__(self):  
        Sprite.__init__(self)
        self.image = image.load("filename").convert()