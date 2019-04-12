import pygame
import os

way_to_pictures = os.path.dirname(__file__)

game_window = pygame.display.set_mode((1005, 630))
pygame.display.set_caption('Pong') 

background = pygame.image.load(os.path.join(way_to_pictures, 'sprites/fon.png'))
draw_background = game_window.blit(background, (0, 0))