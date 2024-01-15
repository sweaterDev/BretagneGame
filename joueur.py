from pygame import *
from pygame.sprite import *
class Joueur:
    
    def __init__(self, image_path, position_initiale, vitesse, saut):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (150, 180))
        self.rect = self.image.get_rect(midbottom=position_initiale)
        self.vitesse = vitesse
        self.saut = saut
        self.y_vitesse = 0
        self.on_ground = False
        self.live = 3
        self.score = 0
        self.position_initial = position_initiale[0] *2
    def move(self, keys, ground_height, screen_height):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vitesse
        if keys[pygame.K_RIGHT] and self.rect.right < self.position_initial:
            self.rect.x += self.vitesse
        if keys[pygame.K_SPACE] and self.on_ground:
            self.y_vitesse = -self.saut
            self.on_ground = False

        # Gravité
        if not self.on_ground:
            self.y_vitesse += 1
            self.rect.y += self.y_vitesse

        # Vérification si le joueur est sur le sol
        if self.rect.bottom >= screen_height - ground_height:
            self.rect.bottom = screen_height - ground_height
            self.on_ground = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        