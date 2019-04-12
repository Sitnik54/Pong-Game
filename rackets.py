import os
import pygame
import background as bg
import ball as bl

vertical_fst_racket = 260
vertical_snd_racket = 260
racket_speed = 15

way_to_pictures = os.path.dirname(__file__)
first_racket = pygame.image.load(os.path.join(way_to_pictures, 'sprites/raket1.png'))
second_racket = pygame.image.load(os.path.join(way_to_pictures, 'sprites/raket2.png'))

def first_racket_movement():
    bg.game_window.blit(bg.background, (0, 0))
    draw_first_racket = bg.game_window.blit(first_racket, (10, vertical_fst_racket))
    draw_second_racket = bg.game_window.blit(second_racket, (980, vertical_snd_racket))

def second_racket_movement():
    bg.game_window.blit(bg.background, (0, 0))
    draw_second_racket = bg.game_window.blit(second_racket, (980, vertical_snd_racket))
    draw_first_racket = bg.game_window.blit(first_racket, (10, vertical_fst_racket))


