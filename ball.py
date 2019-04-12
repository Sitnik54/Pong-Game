import pygame
import random
import score 
import sound
import background as bg
import rackets as rks

ball_horizontal = 505
ball_vertical = 320
ball_speed = 15
direction = random.choice(['down_left', 'up_left', 'up_right', 'down_right'])

def ball_movement():
    global ball_horizontal
    global ball_vertical
    global direction
    if direction == 'up_left':
        ball_vertical += ball_speed
        ball_horizontal -= ball_speed
        bg.game_window.blit(bg.background, (0, 0))
        draw_circle = pygame.draw.circle(bg.game_window, (255, 215, 0), (ball_horizontal, ball_vertical), 8)
        if ball_vertical >= 600:
            sound.sound_ricochet()
            direction = 'down_left'
        restart_ball()
        hit_ball()

    if direction == 'down_left':
        ball_vertical -= ball_speed
        ball_horizontal -= ball_speed
        bg.game_window.blit(bg.background, (0, 0))
        draw_circle = pygame.draw.circle(bg.game_window, (255, 215, 0), (ball_horizontal, ball_vertical), 8)
        if ball_vertical <= 35:
            sound.sound_ricochet()
            direction = 'up_left'
        restart_ball()
        hit_ball()

    if direction == 'up_right':
        ball_vertical += ball_speed
        ball_horizontal += ball_speed
        bg.game_window.blit(bg.background, (0, 0))
        draw_circle = pygame.draw.circle(bg.game_window, (255, 215, 0), (ball_horizontal, ball_vertical), 8)
        if ball_vertical >= 600:
            sound.sound_ricochet()
            direction = 'down_right'
        restart_ball()
        hit_ball()

    if direction == 'down_right':
        ball_vertical -= ball_speed
        ball_horizontal += ball_speed
        bg.game_window.blit(bg.background, (0, 0))
        draw_circle = pygame.draw.circle(bg.game_window, (255, 215, 0), (ball_horizontal, ball_vertical), 8)
        if ball_vertical <= 35:
            sound.sound_ricochet()
            direction = 'up_right'
        restart_ball()
        hit_ball()
    score.score_match()
    rks.draw_second_racket = bg.game_window.blit(rks.second_racket, (980, rks.vertical_snd_racket))
    rks.draw_first_racket = bg.game_window.blit(rks.first_racket, (10, rks.vertical_fst_racket))
    
def restart_ball():
    global ball_horizontal
    global ball_vertical
    global direction
    if ball_horizontal >= 1100 or ball_horizontal <= -100:
            if ball_horizontal >= 1100:
                score.score_match(point_fst_player = 1)
            if ball_horizontal <= -100:
                score.score_match(point_snd_player = 1)
            ball_horizontal = 505
            ball_vertical = random.randint(55, 550) 
            direction = random.choice(['down_left', 'up_left', 'up_right', 'down_right'])

def hit_ball():
    global direction
    if (ball_vertical in range(rks.vertical_fst_racket - 15, rks.vertical_fst_racket + 125) and ball_horizontal in range (10, 35) or 
        ball_vertical in range(rks.vertical_snd_racket - 15, rks.vertical_snd_racket + 125) and  ball_horizontal == 970):
        sound.sound_ricochet()
        if direction == 'up_left':
            direction = 'up_right'
        elif direction == 'down_left':
            direction = 'down_right'
        elif direction == 'down_right':
            direction = 'down_left'
        elif direction == 'up_right':
            direction = 'up_left'
    
