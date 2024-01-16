import pygame
import sys
from pygame.mixer import *
import threading
from Button import Button
from Niveau import Niveau
from Cinematique import Cinematique
# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
info_ecran = pygame.display.Info()
largeur_ecran = info_ecran.current_w
hauteur_ecran = info_ecran.current_h
screen = pygame.display.set_mode((largeur_ecran,hauteur_ecran))
background_menu = pygame.image.load("images\menu_background.png")
background_img = pygame.transform.scale(background_menu, (hauteur_ecran,largeur_ecran))
screen_size_x,screen_size_y = pygame.display.get_window_size()

b_niveau_1 = Button(screen_size_x /2 - 200 /2, screen_size_y /2 - 50/2,300,50,"Niveau 1")
b_niveau_2 = Button(screen_size_x /2 - 200 /2,screen_size_y /2 -50/2 +100,300,50,"Niveau 2")
b_niveau_3 = Button(screen_size_x /2- 200 /2,screen_size_y /2 -50/2 +200, 300, 50,"Niveau 3")
b_quitter = Button(100,  100, 200, 50,"Quitter")

def play_music():
    pygame.mixer.music.load("musique\musique_menu.mp3")
    pygame.mixer.music.play(loops=-1)

# Démarrer le thread de musique
music_thread = threading.Thread(target=play_music)
music_thread.start()

def main_menu():
    while True:
        screen.blit(background_menu, (0, 0))
        b_niveau_1.draw_button(screen,(255, 255, 255),(0, 0, 0))
        b_niveau_2.draw_button(screen,(255, 255, 255),(0, 0, 0))
        b_niveau_3.draw_button(screen,(255, 255, 255),(0, 0, 0))
        b_quitter.draw_button(screen, (255, 255, 255),(0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if b_niveau_1.is_clicked(x,y):
                   c1= Cinematique()
                   c1.play_cinematic(screen)
                   niveau1 = Niveau(screen,30,40,60,"images\lv1_background.png","musique\musique_lvl1.mp3")
                   niveau1.run()
                if b_niveau_2.is_clicked(x,y):
                   niveau1 = Niveau(screen,20,40,60,"images\lv2_background.png","musique\musique_lvl2.mp3")
                   niveau1.run()
                if b_niveau_3.is_clicked(x,y):
                   niveau1 = Niveau(screen,10,40,60,"images\lv3_background.png","musique\musique_menu.mp3")
                   niveau1.run()
                if b_quitter.is_clicked(x,y):
                   music.stop()
                   pygame.quit()
                   sys.exit()
                   
            # Ici, ajoutez la logique pour les boutons du menu

        # Mise à jour de l'affichage
        pygame.display.update()



# Appel du menu principal
main_menu()
