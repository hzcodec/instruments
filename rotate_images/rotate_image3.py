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

# define colors
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
BLUE        = (0, 0, 255)
LIGHT_BLUE  = (0, 255, 255)
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)

TIME_DELAY_IN_MS = 200

RIGHT = 3

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
# the green/red rectangles will be equal
offsetX = 30
offsetY = 30

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
screen_rect = screen.get_rect()

image = pygame.image.load('green_car.png')
#image = pygame.image.load('../instruments/needle2.png')

# if convert() is added then the green rectangle is partly hidden by the red rectangle
#image = pygame.image.load('green_car.png').convert()

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

    angle += 10
    if angle > 360:
        angle = 0

    screen.fill(BLACK)

    pygame.draw.line(screen, BLUE, (10,180), (630,180), 2)
    pygame.draw.line(screen, BLUE, (320,10), (320,350), 2)

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    radAngle = math.radians(angle)
    xPos = math.cos(radAngle)*offsetX
    yPos = math.sin(radAngle)*offsetY

    print '-'*60
    print 'angle:',angle,'  -  xPos:',xPos,'  -  yPos:',yPos

    rotatedImageRectangle.center = (320,180)

    # draw a rectangle before compensation of the angle
    pygame.draw.rect(screen, GREEN, (rotatedImageRectangle[0],
                                     rotatedImageRectangle[1],
                                     rotatedImageRectangle[2],
                                     rotatedImageRectangle[3]), 1)

    print '  Green rectangle before update:',rotatedImageRectangle
    print '  New x:',rotatedImageRectangle[0]+xPos
    print '  New y:',rotatedImageRectangle[1]-yPos

    pygame.draw.line(screen, LIGHT_BLUE, (0,0), (rotatedImageRectangle[0],rotatedImageRectangle[1]), 2)
    

    # ------------------------------------------------------------------------------------------------------
    # Now compensate rectangle due to the angle.
    # Only indexes [0] and [1] in rotatedImageRectangle are updated.
    # ------------------------------------------------------------------------------------------------------
    rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * offsetX,
                                   -np.sin(math.radians(angle)) * offsetY])

    print '  Red rectangle after update:',rotatedImageRectangle

    # blit rotated image
    screen.blit(rotatedImage, rotatedImageRectangle)

    # draw a rectangle around the image after compensation of the angle
    pygame.draw.rect(screen, RED, (rotatedImageRectangle[0],
                                   rotatedImageRectangle[1],
                                   rotatedImageRectangle[2],
                                   rotatedImageRectangle[3]),
                                   1)

    pygame.draw.line(screen, LIGHT_BLUE, (0,0), (rotatedImageRectangle[0],rotatedImageRectangle[1]), 2)

    pygame.display.update()
    pygame.time.delay(TIME_DELAY_IN_MS)

