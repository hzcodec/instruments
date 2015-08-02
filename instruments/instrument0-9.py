import pygame, sys
from pygame.locals import *
import os

# define constants related to window size and button positions
X_BUTTON = 200 
Y_BUTTON = 100 
(WIDTH, HEIGHT) = (800, 600)
BLACK = (0,0,0)

# setup button positions
DIAL_POS  = (X_BUTTON, Y_BUTTON)

# center window on monitor
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

# load button images
dial = pygame.image.load('instrument0-9.png')

indexFont = pygame.font.SysFont("None",48)

# fix background color to white
background = pygame.Surface(screen.get_size())
background.fill((0,100,100))
screen.blit(background,(0, 0))

# blit buttons on screen
screen.blit(dial,(DIAL_POS))

pygame.display.flip()

toggle = True

while True:

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

