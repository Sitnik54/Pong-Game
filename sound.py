import os
import pygame

pygame.mixer.init()
way_to_sound = os.path.dirname(__file__)

def sound_intro(stop = False):
    pygame.mixer.music.load(os.path.join(way_to_sound, 'sound/intro.ogg'))
    pygame.mixer.music.play(-1)
    if stop == True:
        pygame.mixer.music.stop()
        
def sound_ricochet():
    ricochet = pygame.mixer.Sound(os.path.join(way_to_sound, 'sound/ricochet.ogg'))
    ricochet.play(0)

        
