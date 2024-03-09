#customised scoreboard

#imports stuff which means it works
import pygame #import pygame
import sys #imports system
import random #imports random
from pygame.locals import *
pygame.init()

#sets width and height of scoreboard (might be able to change, wouldn't recommend)
width = 1050
height = 100

#sets fps and pressed variable (do not change)
fps = 30
pressed = False

#sets variables for background colour (default red) using hex values, score text colour (default black, also uses hex codes), and the font which the score is written (first value is font itself, second is size (don't change the size))
background_colour = (255, 156, 29)
score_colour = (0, 0, 0)
font = pygame.font.SysFont('Ariel', 70)

#sets the starting score for both teams
team_a_score = 0
team_b_score = 0

#loads the Duck5goQuack banner, Team A logo and Team B logo, ONLY CHANGE THE COMMENTED LINES
ducklogo = pygame.image.load('Duck5goQuack (10).png')
team_a_l = pygame.image.load('Guinea_Fortuna.png') #this can be changed to the team of your choosing
a_scale = height / team_a_l.get_height()
a_width = int(team_a_l.get_width() * a_scale)
team_a_logo = pygame.transform.scale(team_a_l, (a_width, height))
team_b_l = pygame.image.load('Acceleron Maracaibo.png') #this can be changed to the team of your choosing
b_scale = height / team_b_l.get_height()
b_width = int(team_b_l.get_width() * b_scale)
team_b_logo = pygame.transform.scale(team_b_l, (b_width, height))

#creates the scoreboard window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scoreboard')

#cooldown for changing the score, wouldn't recommend changing
cooldown_duration = 1000
last_press_time = 0

#main code loop
run = True
while run:
    screen.fill(background_colour) #draws background colour, changable higher up
    screen.blit(ducklogo, (0, 0)) #draws duck banner
    screen.blit(team_a_logo, (ducklogo.get_width(), 0)) #draws a team logo, changable higher up
    screen.blit(team_b_logo, (width - (team_b_logo.get_width()), 0)) #draws b team logo, changeable higher up

    for event in pygame.event.get(): #allows you to close the window
        if event.type == pygame.QUIT:
            run = False

    current_time = pygame.time.get_ticks() #change scores
    key = pygame.key.get_pressed()
    if key[pygame.K_F9] and current_time - last_press_time > cooldown_duration: #change F9 to key of choosing which REDUCES team a score
        team_a_score -= 1 
        last_press_time = current_time 
    if key[pygame.K_F10] and current_time - last_press_time > cooldown_duration: #change F10 to key of choosing which INCREASES team a score
        team_a_score += 1
        last_press_time = current_time
    if key[pygame.K_F11] and current_time - last_press_time > cooldown_duration: #change F11 to key of choosing which INCREASES team b score
        team_b_score += 1
        last_press_time = current_time
    if key[pygame.K_F12] and current_time - last_press_time > cooldown_duration: #change F12 to key of choosing which REDUCES team b score
        team_b_score -= 1
        last_press_time = current_time

    #creates the text for scores
    team_a_scoretext = font.render(str(team_a_score), True, score_colour) 
    team_b_scoretext = font.render(str(team_b_score), True, score_colour)

    #draws the score text
    screen.blit(team_a_scoretext, ((ducklogo.get_width() + team_a_logo.get_width() + 10, 50 - (team_a_scoretext.get_height() // 2))))
    screen.blit(team_b_scoretext, ((width - team_b_logo.get_width()) - 10 - team_b_scoretext.get_width(), 50 - (team_b_scoretext.get_height() // 2)))

    #updates
    pygame.display.flip()
    pygame.display.update()