import pygame

game_session = True
def quit():
    global game_session
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_session = False 
                 