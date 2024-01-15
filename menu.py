import pygame
import sys
from pygame.mixer import *
import threading

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre de jeu
screen = pygame.display.set_mode((1920, 1080),pygame.FULLSCREEN)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)
background_menu = pygame.image.load("Menu_background.png")
background_img = pygame.transform.scale(background_menu, (1920, 1080))
background_niveau_1 = pygame.image.load("lv1_background.png")

def draw_button(screen, text, x, y, width, height):
    pygame.draw.rect(screen, WHITE, [x, y, width, height])
    text_render = font.render(text, True, BLACK)
    screen.blit(text_render, (x + (width - text_render.get_width()) // 2, y + (height - text_render.get_height()) // 2))

def play_music():
    pygame.mixer.music.load("Music_Menu.mp3")
    pygame.mixer.music.play(loops=-1)

# Démarrer le thread de musique
music_thread = threading.Thread(target=play_music)
music_thread.start()

def main_menu():
    while True:
        screen.blit(background_menu, (0, 0))
        screen_size_x,screen_size_y = pygame.display.get_window_size()
        draw_button(screen, "Niveau 1", screen_size_x /2 - 200 /2, screen_size_y /2 - 50/2 , 200, 50)
        draw_button(screen, "Niveau 2", screen_size_x /2 - 200 /2, screen_size_y /2 -50/2 +100, 200, 50)
        draw_button(screen, "Niveau 3", screen_size_x /2- 200 /2, screen_size_y /2 -50/2 +200, 200, 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                music.stop()
                pygame.quit()
                sys.exit()
                
            # Ici, ajoutez la logique pour les boutons du menu

        # Mise à jour de l'affichage
        pygame.display.update()

def niveau_1():
    # Logique pour le niveau 1
    pass

def niveau_2():
    # Logique pour le niveau 2
    pass

def niveau_3():
    # Logique pour le niveau 3
    pass

# Appel du menu principal
main_menu()
