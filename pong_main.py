import pygame
import os
import func_quit as fq
import func_preview as fp
import rackets as rks
import ball as bl
   
pygame.init()
fp.preview()
fp.startscreen()
clock = pygame.time.Clock()
while fq.game_session: 
    clock.tick(30)
    fq.quit()   
    key = pygame.key.get_pressed() 
    if key[pygame.K_w] and rks.vertical_fst_racket >= 40: 
        rks.vertical_fst_racket -= rks.racket_speed
        rks.first_racket_movement()
         
    if key[pygame.K_s] and rks.vertical_fst_racket < 490: 
        rks.vertical_fst_racket += rks.racket_speed
        rks.first_racket_movement()
    
    if key[pygame.K_UP] and rks.vertical_snd_racket >= 40:
        rks.vertical_snd_racket -= rks.racket_speed
        rks.second_racket_movement()
    
    if key[pygame.K_DOWN] and rks.vertical_snd_racket < 490:
        rks.vertical_snd_racket += rks.racket_speed
        rks.second_racket_movement()
    bl.ball_movement()  
    pygame.display.update()

pygame.quit()