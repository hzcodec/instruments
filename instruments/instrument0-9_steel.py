# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : rotate_image2.py
# Reference   : -
# Description : Rotate the loaded image at an offset position.
#               The position is set by offsetX and offsetY.
#               Same as rotation_image2 but now rotating without mouse controll.
#               Instead the rotation speed is set by TIME_DELAY_IN_MS.
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

TIME_DELAY_IN_MS = 200
X_DIAL_COORD   = 200 
Y_DIAL_COORD   = 100 
X_NEEDLE_COORD = 400 
Y_NEEDLE_COORD = 300 
DIAL_POS   = (X_DIAL_COORD, Y_DIAL_COORD)
NEEDLE_POS = (X_NEEDLE_COORD, Y_NEEDLE_COORD)

RIGHT = 3

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
offsetX = 55
offsetY = 55

pygame.init()

# center window on monitor
os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((800, 600), 0, 32)
screen_rect = screen.get_rect()

dial  = pygame.image.load('instrument0-9.png') #.convert()
image = pygame.image.load('needle2.png')

imageRectangle = image.get_rect()
center = imageRectangle.center

print 'Rectangle:',imageRectangle
print 'Center:',center

background = pygame.Surface(screen.get_size())
background = background.convert()

angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    angle += 2
    if angle > 360:
        angle = 0

    screen.fill(STEEL)
    screen.blit(dial, (DIAL_POS))

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    radAngle = math.radians(angle)
    xPos = math.cos(radAngle)*offsetX
    yPos = math.sin(radAngle)*offsetY

    rotatedImageRectangle.center = (NEEDLE_POS)

    # ----------------------------------------------------------------------------------------
    # Now compensate rectangle due to the angle.
    # Only indexes [0] and [1] in rotatedImageRectangle are updated.
    # ----------------------------------------------------------------------------------------
    rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                   -np.sin(math.radians(angle)) * offsetY])

    # blit rotated image
    screen.blit(rotatedImage, rotatedImageRectangle)

    pygame.display.update()
    pygame.time.delay(TIME_DELAY_IN_MS)

