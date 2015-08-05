# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : instrument0-9_rot2.py
# Reference   : -
# Description : Instrument is rotated.
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


def help_lines(screen):
    """
    Draw help lines in the middle of the screen. Only used for test purpose.
    """
    pygame.draw.line(screen, RED, (10,Y_NEEDLE_COORD), (790,Y_NEEDLE_COORD))
    pygame.draw.line(screen, RED, (X_NEEDLE_COORD,10), (X_NEEDLE_COORD,590))


def scan_keyboard(angle):
   """
   Scan keyboard and set requested angle.
   """
   requestedAngle = angle

   # static variable
   if not hasattr(scan_keyboard, "inputData"):
       scan_keyboard.inputData = 0

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_z:
           scan_keyboard.inputData += 1
           if scan_keyboard.inputData > 9:
               scan_keyboard.inputData = 9
           requestedAngle = int(-36*scan_keyboard.inputData + 270)

       elif event.type == KEYDOWN and event.key == pygame.K_x:
           scan_keyboard.inputData -= 1
           if scan_keyboard.inputData < 0:
               scan_keyboard.inputData = 0
           requestedAngle = int(-36*scan_keyboard.inputData + 270)

   return requestedAngle


class Needle():
    def __init__(self, screen):
        needle = pygame.image.load('needle2.png')
        

class Instrument():
    def __init__(self, screen):
        self.screen = screen
        self.dial = pygame.image.load('instrument0-9.png')
        self.needle = pygame.image.load('needle2.png')

    def rotate(self, angle):
        self.rotatedImage = pygame.transform.rotate(self.needle, angle)
        self.rotatedImageRectangle = self.rotatedImage.get_rect()
    
        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (NEEDLE_POS)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * 55,
                                            -np.sin(math.radians(angle)) * 55])
    
        self.update()

    def update(self):
        self.screen.blit(self.dial, (DIAL_POS))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)



def main():
    
    # center window on monitor
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    instrument = Instrument(screen)
    
    # make mouse pointer invisible
    pygame.mouse.set_visible(False)
    
    # set at 0 position
    angle = 270
    currentAngle = 270
    
    while True:
        requestedAngle = scan_keyboard(currentAngle)
        currentAngle = requestedAngle

        screen.fill(STEEL)
        instrument.rotate(currentAngle)
    
        # draw help line for test purpose
        #help_lines(screen)
    
        # draw a black middle circle at needle
        pygame.draw.circle(screen, BLACK, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 23, 0)
        pygame.draw.circle(screen, WHITE, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 5, 0)
    
        pygame.display.update()


if __name__ == '__main__':
    main()
