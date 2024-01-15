from pygame import *
from pygame.sprite import *
from objet import objet
class name(objet):
    def __init__(self):  
        Sprite.__init__(self)
        self.image = image.load("filename").convert()
        self.rect = self.image.get_rect().move(x, y)