import background as bg
import pygame
import os
import sound

way_to_pictures = os.path.dirname(__file__)
fon_preview = pygame.image.load(os.path.join(way_to_pictures, 'sprites/preview.png'))
def preview():
    sound.sound_intro()
    start_ticks = pygame.time.get_ticks() 
    while True:
        bg.game_window.blit(fon_preview,(0,0))       
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000 
        if seconds > 5: 
            break
        pygame.display.flip()

preview_session = True
fon_startscreen = pygame.image.load(os.path.join(way_to_pictures, 'sprites/startscreen.png'))
def startscreen():
    global preview_session
    while preview_session == True: 
        bg.game_window.blit(fon_startscreen,(0,0))
        startscreen_label = os.path.join(way_to_pictures, 'sprites/scorefont.ttf')
        startscreen_label = pygame.font.Font(startscreen_label, 32)
        startscreen_text = startscreen_label.render('Press Enter to start!', True, (255, 215, 0))
        bg.game_window.blit(startscreen_text, (40, 50))
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RETURN:
                    sound.sound_intro(stop = True)
                    preview_session = False
        pygame.display.flip()
