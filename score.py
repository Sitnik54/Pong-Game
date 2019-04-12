import os
import pygame
import background as bg

way_to_pictures = os.path.dirname(__file__)
score_fst_player = 0
score_snd_player = 0

def score_match(point_fst_player = 0, point_snd_player = 0, font_color = (255, 255, 255), 
                font_type = os.path.join(way_to_pictures, 'sprites/scorefont.ttf'), font_size = 50):
    global score_fst_player
    global score_snd_player
    score_fst_player += point_fst_player
    score_snd_player += point_snd_player
    font_type = pygame.font.Font(font_type, font_size)
    text_score_fst_player = font_type.render(str(score_fst_player), True, font_color)
    text_score_snd_player = font_type.render(str(score_snd_player), True, font_color)
    
    if score_fst_player >= 10:
        bg.game_window.blit(text_score_fst_player, (400, 40))
    else:
        bg.game_window.blit(text_score_fst_player, (430, 40))
    
    if score_snd_player >= 10:
        bg.game_window.blit(text_score_snd_player, (530, 40))
    else:
        bg.game_window.blit(text_score_snd_player, (540, 40))

