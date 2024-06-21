#customised scoreboard

#imports stuff which means it works
import pygame #import pygame
import sys #imports system
from pygame.locals import *
from pynput.keyboard import Key, Listener
pygame.init()

#sets width and height of scoreboard (might be able to change, wouldn't recommend)
width = 1920
height = 330

#sets fps and pressed variable (do not change)
fps = 30
pressed = False

#sets variables for score text colour (default black, also uses hex codes), and the font which the score is written (first value is font itself, second is size (don't change the size))
score_colour = (0, 0, 0)
font = pygame.font.SysFont('Ariel', 70)

#sets the starting score for both teams
a_score = 0
b_score = 0

#loads the scoreboard image
sb_img = pygame.image.load('new_scoreboard.png')

#creates the scoreboard window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scoreboard')

#cooldown for changing the score, wouldn't recommend changing
cooldown_duration = 1000
last_press_time = 0

def on_press(key, a_score, b_score):
    if key == Key.f9: #change F9 to key of choosing which REDUCES team a score
        a_score -= 1 
    if key == Key.f10: #change F10 to key of choosing which INCREASES team a score
        a_score += 1
    if key == Key.f11: #change F11 to key of choosing which INCREASES team b score
        b_score += 1
    if key == Key.f12: #change F12 to key of choosing which REDUCES team b score
        b_score -= 1

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#main code loop
run = True
while run:
    screen.blit(sb_img, (0, 0)) #draws scoreboard image

    for event in pygame.event.get(): #allows you to close the window
        if event.type == pygame.QUIT:
            run = False

    current_time = pygame.time.get_ticks() #change scores

    on_press(a_score, b_score)
    on_release()

    #creates the text for scores
    team_a_scoretext = font.render(str(a_score), True, score_colour) 
    team_b_scoretext = font.render(str(b_score), True, score_colour)

    #creates the text for team names
    a_name = font.render("ABC", True, score_colour) 
    b_name = font.render("XYZ", True, score_colour)

    #draws the score and name text
    screen.blit(team_a_scoretext, (0, 0))
    screen.blit(team_b_scoretext, (10, 0))

    #screen.blit(a_name, (0, 0))
    #screen.blit(b_name, (0, 0))

    #updates
    pygame.display.flip()
    pygame.display.update()