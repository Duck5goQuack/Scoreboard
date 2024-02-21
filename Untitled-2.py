#customised scoreboard

import pygame #import pygame
import sys #imports system
import random #imports random
from pygame.locals import *
pygame.init()

width = 1050
height = 100

fps = 30
pressed = False

background_colour = (255, 0, 0)
score_colour = (0, 0, 0)
font = pygame.font.SysFont('Ariel', 70)

team_a_score = 0
team_b_score = 0

ducklogoload = pygame.image.load('Duck5goQuack (9).png')
ducklogo = pygame.transform.scale(ducklogoload, (ducklogoload.get_width()*3, ducklogoload.get_height()*3))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scoreboard')

cooldown_duration = 1000
last_press_time = 0

run = True
while run:
    screen.fill(background_colour)
    screen.blit(ducklogo, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_time = pygame.time.get_ticks()
    key = pygame.key.get_pressed()
    if key[pygame.K_F9] and current_time - last_press_time > cooldown_duration:
        team_a_score -= 1 
        last_press_time = current_time 
    if key[pygame.K_F10] and current_time - last_press_time > cooldown_duration:
        team_a_score += 1
        last_press_time = current_time
    if key[pygame.K_F11] and current_time - last_press_time > cooldown_duration:
        team_b_score += 1
        last_press_time = current_time
    if key[pygame.K_F12] and current_time - last_press_time > cooldown_duration:
        team_b_score -= 1
        last_press_time = current_time

    team_a_scoretext = font.render("TeA " + str(team_a_score), True, score_colour)
    team_b_scoretext = font.render(str(team_b_score) + " TeB", True, score_colour)

    screen.blit(team_a_scoretext, (10, 10))
    screen.blit(team_b_scoretext, ((width - team_b_scoretext.get_width()) - 10, 10))

    pygame.display.flip()
    pygame.display.update()