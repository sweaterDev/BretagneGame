import pygame
class Cinematique:
    # ... autres méthodes ...

    
    def __init__(self,sound_path,duration,text):
        self.duration = duration
        self.text = text
        self.sound_path = sound_path
        self.screen_size_x,self.screen_size_y = pygame.display.get_window_size()
            
    def play_cinematic(self, screen):
        pygame.mixer.music.load(self.sound_path)
        pygame.mixer.music.play(loops=1)
        font = pygame.font.Font("eltirg__.ttf", 36)
        lines = self.text.split('\n')  # Diviser le texte en lignes

        
        

        # Position de départ pour le premier texte
        start_y = self.screen_size_y

        start_time = pygame.time.get_ticks()
        text_finished = False

        while not text_finished:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return  # Sortir de la méthode pour passer la cinématique

            screen.fill((0, 0, 0))  # Effacer l'écran

            y_offset = 0
            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.screen_size_x / 2, start_y + y_offset))
                screen.blit(text_surface, text_rect)
                y_offset += text_surface.get_height() + 7  # Espacement entre les lignes

            start_y -= 0.1  # Vitesse de défilement
            if start_y < -y_offset or current_time - start_time > self.duration:  # 10 secondes par exemple
                text_finished = True

              # Afficher l'option pour passer
            pygame.display.flip()  # Mettre à jour l'écran
