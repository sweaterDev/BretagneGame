from Button import Button
from Cinematique import Cinematique


from CinematiqueMortController import CinematiqueMortController
import pygame
class CinematiqueMort :
    def __init__(self,level_id) :
        self.screen_size_x,self.screen_size_y = pygame.display.get_window_size()
        self.retry_button = Button( self.screen_size_x / 2 - 50, self.screen_size_y / 2, 100,100, "Retry")
        self.menu_button = Button( self.screen_size_x / 2 - 50, self.screen_size_y / 2 + 60, 100,100, "Menu")
        self.level_id = level_id
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
            
            pygame.display.flip()
