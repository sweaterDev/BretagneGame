from Button import Button
from Cinematique import Cinematique
import csv


from CinematiqueMortController import CinematiqueMortController
import pygame
class CinematiqueMort :
    def __init__(self,level_id) :
        self.screen_size_x,self.screen_size_y = pygame.display.get_window_size()
        self.retry_button = Button( self.screen_size_x / 2 - 50, self.screen_size_y / 2, 100,100, "Retry")
        self.menu_button = Button( self.screen_size_x / 2 - 50, self.screen_size_y / 2 + 150, 100,100, "Menu")
        self.level_id = level_id
        self.highscore_file = f"highscore.csv"
        self.highscore = self.lire_highscore()
        self.cinematique_controller = CinematiqueMortController()
        self.mouse_pose_x,self.mouse_pose_y = pygame.mouse.get_pos()
    def play_cinematic(self, screen):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.retry_button.is_clicked(event.pos):
                        self.cinematique_controller.retry_level(screen,self.level_id)
                    elif self.menu_button.is_clicked(event.pos):
                        return
                
            screen.fill((0, 0, 0))
            self.retry_button.draw_button(screen,(255,255,255))
            self.menu_button.draw_button(screen,(255,255,255))
            self.afficher_highscore(screen)
            
            pygame.display.flip()
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
        
    def afficher_highscore(self, screen):
        font = pygame.font.Font(None, 36)  # Utilisez la police souhaitée
        highscore_text = font.render(f"Highscore: {self.highscore}", True, (255, 255, 255))  # Blanc
        text_rect = highscore_text.get_rect(topright=(self.screen_size_x - 1310, 110))  # Position en haut à droite
        screen.blit(highscore_text, text_rect)