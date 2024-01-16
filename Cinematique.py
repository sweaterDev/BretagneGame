import pygame
class Cinematique:
    # ... autres méthodes ...

    
    def __init__(self):
        self.text = [ "Texte pour la première image",  "Texte pour la deuxième image","Texte pour la troisième image", "Texte pour la quatrième image"]
        self.images = [pygame.transform.scale(pygame.image.load(f"cinematique\images{i}.png"),(150,150)) for i in range(1, 5)]
        self.screen_size_x,self.screen_size_y = pygame.display.get_window_size()
            
    def play_cinematic(self, screen):
        for i in range(4):
            # Afficher chaque image avec son texte
            screen.fill((0, 0, 0))  # Effacer l'écran
            screen.blit(self.images[i], (self.screen_size_x/2 -150, self.screen_size_y/2 -150))  # Coordonnées de l'image

            # Afficher le texte
            font = pygame.font.Font(None, 36)
            text = font.render(self.text[i], True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.screen_size_x/2, self.screen_size_y/2))  # Ajuster les coordonnées
            screen.blit(text, text_rect)

            pygame.display.flip()  # Mettre à jour l'écran
            pygame.time.delay(1000)  # Délai pour chaque image (5000 ms = 5 secondes)

            # Vérifier les événements (par exemple, pour quitter)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
