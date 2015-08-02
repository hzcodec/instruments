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
X_DIAL_COORD   = 200 
Y_DIAL_COORD   = 100 
X_NEEDLE_COORD = 365 
Y_NEEDLE_COORD = 280 

(WIDTH, HEIGHT) = (800, 600)
BLACK = (0,0,0)
RED   = (255,0,0)

# setup button positions
DIAL_POS   = (X_DIAL_COORD, Y_DIAL_COORD)
NEEDLE_POS = (X_NEEDLE_COORD, Y_NEEDLE_COORD)

# center window on monitor
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

# load button images, if convert() is used then the background is affected
dial   = pygame.image.load('instrument0-9.png') #.convert()
needle = pygame.image.load('needle2.png')

# fix background
background = pygame.Surface(screen.get_size())
background.fill((0,100,100))
screen.blit(background,(0, 0))

# blit dial on the screen
screen.blit(dial,(DIAL_POS))
screen.blit(needle,(NEEDLE_POS))

# draw help line
#pygame.draw.line(screen, RED, (10,300), (790,300))
#pygame.draw.line(screen, RED, (400,10), (400,590))

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

