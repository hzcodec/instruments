# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : instrument0-9.py
# Reference   : -
# Description : Just loading one image of a dial.
#
# Python ver : 2.7.3 (gcc 4.6.3)

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

# load button images, if convert() is used then the background is affected
dial = pygame.image.load('instrument0-9.png') #.convert()

# fix background
background = pygame.Surface(screen.get_size())
background.fill((0,100,100))
screen.blit(background,(0, 0))

# blit dial on the screen
screen.blit(dial,(DIAL_POS))

pygame.display.flip()

toggle = True

while True:

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
       elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()

