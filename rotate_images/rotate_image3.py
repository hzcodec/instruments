# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : rotate_image3.py
# Reference   : -
# Description : Rotate the loaded image at an offset position.
#               The position is set by offsetX and offsetY.
#               Same as rotation_image2 but now rotating without mouse controll.
#               Instead the rotation speed is set by TIME_DELAY_IN_MS.
#
#               The offset can be changed by 1-5.
#               Type 'r' to rotate step by step.
#               Type 'c' to rotate continously.
#               Type 's' to stop rotation.
#               Type 'esc' to exit application.
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

TIME_DELAY_IN_MS = 100

# set rotation offset
# if offset = 0 the rotation is around the middle of the image
# the green/red rectangles will be equal
offsetX = 0
offsetY = 0

# position window on monitor
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(800,100)

pygame.init()
screen = pygame.display.set_mode((640, 360), 0, 32)
screen_rect = screen.get_rect()

image = pygame.image.load('green_car.png')

# if convert() is added then the green rectangle is partly hidden by the red rectangle
#image = pygame.image.load('green_car.png').convert()

imageRectangle = image.get_rect()
center = imageRectangle.center

background = pygame.Surface(screen.get_size())

background = background.convert()

angle     = 0
hit       = False  # if 'r' is typed => rotate one step
hit2      = False  # if 'c' is typed => continously rotation
newOffset = False  # if 1-5 is typed 
newAngle  = 0
oldAngle  = 99
rotateDir = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # rotate in increments
        elif event.type == KEYDOWN and event.key == pygame.K_r:
            hit = True
            rotateDir = True

        # rotate in increments
        elif event.type == KEYDOWN and event.key == pygame.K_t:
            hit = True
            rotateDir = False

        # rotate in continously
        elif event.type == KEYDOWN and event.key == pygame.K_c:
            hit2 = True

        # stop continously rotation
        elif event.type == KEYDOWN and event.key == pygame.K_s:
            hit2 = False

        # change offset to the middle of the image
        elif event.type == KEYDOWN and event.key == pygame.K_1:
            offsetX = 0
            offsetY = 0
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_2:
            offsetX = 10
            offsetY = 10
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_3:
            offsetX = 30
            offsetY = 30
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_4:
            offsetX = 60
            offsetY = 60
            newOffset = True

        elif event.type == KEYDOWN and event.key == pygame.K_5:
            offsetX = 90
            offsetY = 90
            newOffset = True

    if hit == True or hit2 == True:
        if rotateDir:
            angle += 5
        else:
            angle -= 5
        if angle > 360:
            angle = 0
        hit = False
        newAngle = angle

    screen.fill(BLACK)

    pygame.draw.line(screen, BLUE, (10,180), (630,180), 2)
    pygame.draw.line(screen, BLUE, (320,10), (320,350), 2)

    rotatedImage = pygame.transform.rotate(image, angle)
    rotatedImageRectangle = rotatedImage.get_rect()

    radAngle = math.radians(angle)
    xPos = math.cos(radAngle)*offsetX
    yPos = math.sin(radAngle)*offsetY

    rotatedImageRectangle.center = (320,180)

    # draw a rectangle before compensation of the angle
    pygame.draw.rect(screen, GREEN, (rotatedImageRectangle[0],
                                     rotatedImageRectangle[1],
                                     rotatedImageRectangle[2],
                                     rotatedImageRectangle[3]), 1)

    if newAngle != oldAngle or newOffset:
        print '-'*60
        print 'angle:',angle,'  -  xPos:',xPos,'  -  yPos:',yPos
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

    
    if newAngle != oldAngle or newOffset:
        print '  Red rectangle after update:',rotatedImageRectangle
        newOffset = False

    oldAngle = newAngle

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

