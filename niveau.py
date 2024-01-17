import pygame
import sys
import random
import csv
from Joueur  import Joueur
from Cinematique import Cinematique
from CinematiqueMortController import CinematiqueMortController
from CinematiqueMort import CinematiqueMort
import serial
from objets.ObjetBonus import ObjetBonus
from objets.ObjetMalus import ObjetMalus
from objets.ObjetSpeciaux import ObjetSpeciaux


class Niveau:
    def __init__(self, screen, player_speed, object_frequency, total_time, background_img_path, music_path,level_id):
        self.WIDTH, self.HEIGHT = screen.get_width(), screen.get_height()
        self.GROUND_HEIGHT = 0
        self.FPS = 60
        self.screen = screen  
        self.joueur = Joueur((self.WIDTH // 2, self.HEIGHT), player_speed, 20)
        self.object_frequency = object_frequency
        self.total_time = total_time
        self.music_path = music_path
        self.start_ticks = pygame.time.get_ticks()
        self.level_id = level_id
        self.highscore_file = f"highscore.csv"
        self.highscore = self.lire_highscore()
        self.cinematique_mort = CinematiqueMort(self.level_id)
        
        # Couleurs
        self.WHITE = (255, 255, 255)
        

        # Chargement et redimensionnement des images
        self.background_img = pygame.transform.scale(pygame.image.load(background_img_path), (self.WIDTH, self.HEIGHT))
        self.life_img = pygame.transform.scale(pygame.image.load("images/life_def.png"), (80, 80))

        self.objects = []
        self.object_counter = 0

        self.font = pygame.font.Font(None, 36)
        self.pause = False
        self.ser = serial.Serial('COM8', 115200)

    def run(self):
       
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(loops=-1)

        while self.total_time > 0 and self.joueur.live > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_port_serie()
                    pygame.quit()
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Utiliser 'p' pour basculer la pause
                        self.toggle_pause()
                    
            if not self.pause:
            # Mettre à jour le jeu si ce n'est pas en pause
                self.update_game()

            else:
            # Afficher l'écran de pause
                self.show_pause_screen()

            self.render()
        if self.joueur.live ==0:
             
            self.close_port_serie()
            self.cinematique_mort.play_cinematic(self.screen)
            
        self.close_port_serie()
        self.verifier_et_maj_highscore(self.joueur.score)  

            

    def generate_random_object(self, frequence):
        chosen_type = random.choice(frequence)
        position_initiale = (random.randint(0, self.WIDTH), 0)
        vitesse = 3

        if chosen_type == 'bonus':
            return ObjetBonus(position_initiale, vitesse)
        elif chosen_type == 'malus':
            return ObjetMalus(position_initiale, vitesse)
        elif chosen_type == 'special':
            return ObjetSpeciaux(position_initiale, vitesse)
    
        
    def show_pause_screen(self):
        pause_text = self.font.render("Jeu en pause. Appuyez sur 'p' pour continuer", True, self.WHITE)
        text_rect = pause_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))  # Centrer le texte
        self.screen.blit(pause_text, text_rect)
        
    def read_sensor(self):
        if self.ser.in_waiting > 0:
            line = self.ser.readline().decode('utf-8').rstrip()

        # Vérifier si la ligne n'est pas vide et représente un nombre
            if line:
                try:
                    return float(line)
                except ValueError:
                    print(f"Erreur de conversion : '{line}' n'est pas un float valide.")
                return None  # Retourner None si la conversion échoue

        return None  # Retourner None si aucune donnée n'est en attente

        
    def update_game(self):
        
        distance = self.read_sensor()
        if distance is not None:
            print(distance)
            if distance < 500.0 :
                self.joueur.move_right()
            elif distance > 750. and distance <1500:
                self.joueur.move_left()
            else :
                self.joueur.stop()
                
            
        

            # Gestion des objets
        self.object_counter += 1
        if self.object_counter == self.object_frequency:
                self.object_counter = 0
                nouvel_objet = self.generate_random_object(['bonus', 'bonus', 'bonus', 'malus', 'special'])
                self.objects.append(nouvel_objet)

        for objet in list(self.objects):
            objet.update()
            if objet.rect.colliderect(self.joueur.rect):
                    objet.son.play()
                    objet.action(self.joueur)  # Appliquer l'effet de l'objet
                    self.objects.remove(objet)
                    
        seconds = (pygame.time.get_ticks() - self.start_ticks) // 1000  # Convertir en secondes
        self.total_time = max(0, 60 - seconds)         
        
                    
    def render(self):
        self.screen.blit(self.background_img, (0, 0))
        for objet in self.objects:
            objet.draw(self.screen)

        self.joueur.draw(self.screen)
            
            # Affichage du temps et des vies
        self.screen.blit(self.joueur.image, self.joueur.rect)
        time_text = self.font.render(f"Time: {self.total_time}s", True, self.WHITE)
        self.screen.blit(time_text, (80, 30))

            # Affichage du score
        score_text = self.font.render(f"Score: {self.joueur.score}", True, self.WHITE)
        self.screen.blit(score_text, (80, 70))
        
        self.afficher_highscore(self.screen)
            
        for i in range(self.joueur.live):
            self.screen.blit(self.life_img, (self.WIDTH - 120 - i * 100, 10))
        pygame.display.flip()
        pygame.time.Clock().tick(self.FPS)
        
    def toggle_pause(self):
        self.pause = not self.pause
    def close_port_serie(self):
        self.ser.close()
        
    def lire_highscore(self):
        try:
            with open(self.highscore_file, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Ignorer l'en-tête
                for row in reader:
                    if row[0] == str(self.level_id):
                        return int(row[1])
            return 0
        except FileNotFoundError:
            return 0

    def sauvegarder_highscore(self, score):
        with open(self.highscore_file, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Niveau', 'Score'])
            writer.writerow([self.level_id, score])
    def verifier_et_maj_highscore(self, nouveau_score):
        if nouveau_score > self.highscore:
            self.highscore = nouveau_score
            self.sauvegarder_highscore(nouveau_score)
    
    def afficher_highscore(self, screen):
        font = pygame.font.Font(None, 36)  # Utilisez la police souhaitée
        highscore_text = font.render(f"Highscore: {self.highscore}", True, (255, 255, 255))  # Blanc
        text_rect = highscore_text.get_rect(topright=(self.WIDTH - 1310, 110))  # Position en haut à droite
        screen.blit(highscore_text, text_rect)