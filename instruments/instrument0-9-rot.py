# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : instrument0-9_rot.py
# Reference   : -
# Description : Instrument is incremented by 'z' and decremented by 'x'.
#
# Python ver : 2.7.3 (gcc 4.6.3)

import pygame
import sys
from pygame.locals import *
import numpy as np
import math
import os

# define colors
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
LIGHT_BLUE  = (0, 255, 255)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
STEEL       = (0, 100, 100)

WIDTH          = 800
HEIGHT         = 600
X_DIAL_COORD   = 200 
Y_DIAL_COORD   = 100 
X_NEEDLE_COORD = 400 
Y_NEEDLE_COORD = 300 

ROTATION_SPEED = 2

DIAL_POS       = (X_DIAL_COORD, Y_DIAL_COORD)
NEEDLE_POS     = (X_NEEDLE_COORD, Y_NEEDLE_COORD)

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
offsetX = 55
offsetY = 55

pygame.init()

# center window on monitor
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
screen_rect = screen.get_rect()

# load images
dial  = pygame.image.load('instrument0-9.png') #.convert()
image = pygame.image.load('needle2.png')

background = pygame.Surface(screen.get_size())
background = background.convert()

pygame.mouse.set_visible(False)

inputData = 0
# set at 0 position
angle = 270

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == pygame.K_z:
            inputData += 1
            if inputData > 9:
                inputData = 9
            angle = int(-36*inputData + 270)

        elif event.type == KEYDOWN and event.key == pygame.K_x:
            inputData -= 1
            if inputData < 0:
                inputData = 0
            angle = int(-36*inputData + 270)
 
    screen.fill(STEEL)
    screen.blit(dial, (DIAL_POS))

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    # compensate for rotation
    radAngle = math.radians(angle)
    xPos = math.cos(radAngle)*offsetX
    yPos = math.sin(radAngle)*offsetY

    rotatedImageRectangle.center = (NEEDLE_POS)
    rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                   -np.sin(math.radians(angle)) * offsetY])

    # blit rotated image
    screen.blit(rotatedImage, rotatedImageRectangle)

    # draw help line for test purpose
    #pygame.draw.line(screen, RED, (10,Y_NEEDLE_COORD), (790,Y_NEEDLE_COORD))
    #pygame.draw.line(screen, RED, (X_NEEDLE_COORD,10), (X_NEEDLE_COORD,590))

    # draw a black middle circle at needle
    pygame.draw.circle(screen, BLACK, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 23, 0)
    pygame.draw.circle(screen, WHITE, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 5, 0)

    pygame.display.update()

