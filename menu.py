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
background_menu = pygame.image.load("images\menu2_background.png")
background_img = pygame.transform.scale(background_menu, (hauteur_ecran,largeur_ecran))
screen_size_x,screen_size_y = pygame.display.get_window_size()
logo_jeu = pygame.transform.scale(pygame.image.load("images\logo_jeu.png"),(300,300))
#Créeation des Boutton
b_niveau_1 = Button(screen_size_x /2 + 500 , screen_size_y /2 - 50/2,300,50,"Niveau 1")
b_niveau_2 = Button(screen_size_x /2 +500 ,screen_size_y /2 -50/2 +100,300,50,"Niveau 2")
b_niveau_3 = Button(screen_size_x /2 +500 ,screen_size_y /2 -50/2 +200, 300, 50,"Niveau 3")
b_quitter = Button(screen_size_x /2 +500 ,screen_size_y /2 -50/2 +350, 300, 50,"Quitter")
Font2_render = pygame.font.Font("Kemco.ttf", 22)
Font = Font2_render.render("© 2024 Lancelot", True, (255, 255, 255))

def play_music():
    pygame.mixer.music.load("musique\musique_menu.mp3")
    pygame.mixer.music.play(loops=-1)

# Démarrer le thread de musique
music_thread = threading.Thread(target=play_music)
music_thread.start()

def main_menu():
    while True:
        
        screen.blit(background_menu, (0, 0))
        screen.blit(Font,(screen_size_x /2 +400, screen_size_y /2 -50/2 +425))
        screen.blit(logo_jeu,(screen_size_x /2 +520 -300/2,screen_size_y /2 -300/2 -250))
        
        b_niveau_1.draw_button(screen,(255, 255, 255))
        b_niveau_2.draw_button(screen,(255, 255, 255))
        b_niveau_3.draw_button(screen,(255, 255, 255))
        b_quitter.draw_button(screen,(255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.stop()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if b_niveau_1.is_clicked(event.pos):
                   c1= Cinematique("sons\cinematique_1.mp3",275000,"En 2063, 15 ans après le Grand Effondrement\nla Bretagne a retrouvé son indépendance\nperdue 531 ans auparavant.\nCependant, le Royaume Normand\nson éternel rival\nest plus menacant que jamais.\nIl faudra donc vous battre afin de récupérer\nsuffisamment de ressources et repousser les envahisseurs.\nVous devez vous rendre à Nantes\nafin de reprendre la ville et commencer\nla réunification de la Bretagne\nBonne chance. ")
                   c1.play_cinematic(screen)
                   niveau1 = Niveau(screen,70,40,60,"images\lv1_background.png","musique\musique_lvl1.mp3",1)
                   niveau1.run()
                if b_niveau_2.is_clicked(event.pos):
                   c2= Cinematique("sons\cinematique_2.mp3",225000,"Nantes est enfin libre\nLa ville a été conquise\n et la province reprise au Royaume perfide\nMais ce n est que le début\nNotre Mont Saint-Michel\npendant longtemps souillé par nos ennemis\nest pret à tomber comme un fruit mur entre nos mains\nIl faut dans un premier temps\n traverser la foret de Brocéliande\noù des cuves de Calvados auraient été apercues.\nLa prudence est de mise. ")
                   c2.play_cinematic(screen) 
                   niveau1 = Niveau(screen,70,40,60,"images\lv2_background.png","musique\musique_lvl2.mp3",2)
                   niveau1.run()
                if b_niveau_3.is_clicked(event.pos):
                   c3 = Cinematique("sons\cinematique_3.mp3",125000,"Nous avons maintenant acquis suffisamment de ressources\npour pouvoir assiéger le Mont.\nVolez les ressources des Normands\net chassez-les de nos terres\nSi vous réussissez\nles portes de la Normandie nous seront alors ouvertes.")
                   c3.play_cinematic(screen)
                   niveau1 = Niveau(screen,70,40,60,"images\lv3_background.png","musique\musique_lvl3.mp3",3)
                   niveau1.run()
                if b_quitter.is_clicked(event.pos):
                   music.stop()
                   pygame.quit()
                   sys.exit()
                   
            # Ici, ajoutez la logique pour les boutons du menu

        # Mise à jour de l'affichage
        pygame.display.update()



# Appel du menu principal
main_menu()
