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

# screen size
WIDTH          = 800
HEIGHT         = 600

X_DIAL_COORD   = 200 
Y_DIAL_COORD   = 100 
X_NEEDLE_COORD = 400 
Y_NEEDLE_COORD = 300 

# rotation offset
OFFSET_X = 55
OFFSET_Y = 55

# postion of dial and needle
DIAL_POS   = (X_DIAL_COORD, Y_DIAL_COORD)
NEEDLE_POS = (X_NEEDLE_COORD, Y_NEEDLE_COORD)


def help_lines(screen):
    """
    Draw help lines in the middle of the screen. Only used for test purpose.
    """
    pygame.draw.line(screen, RED, (10,Y_NEEDLE_COORD), (790,Y_NEEDLE_COORD))
    pygame.draw.line(screen, RED, (X_NEEDLE_COORD,10), (X_NEEDLE_COORD,590))


def instruction():
    """
    Set up instruction.
    """
    instructionFont = pygame.font.SysFont("None",28)
    instr1 = instructionFont.render("Use -> to increment", 0, BLACK)
    instr2 = instructionFont.render("Use <- to decrement", 0, BLACK)
    return instr1, instr2


def scan_keyboard(angle):
   """
   Scan keyboard and set requested angle.
   Escape key => application quit
   Right key  => increment
   Left key   => decrement
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

       elif event.type == KEYDOWN and event.key == pygame.K_RIGHT:
           scan_keyboard.inputData += 1
           if scan_keyboard.inputData > 9:
               scan_keyboard.inputData = 9

       elif event.type == KEYDOWN and event.key == pygame.K_LEFT:
           scan_keyboard.inputData -= 1
           if scan_keyboard.inputData < 0:
               scan_keyboard.inputData = 0

   # calculate angle of needle, 270 degrees => '0'
   requestedAngle = int(-36*scan_keyboard.inputData + 270)
   return requestedAngle


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
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * OFFSET_X,
                                            -np.sin(math.radians(angle)) * OFFSET_Y])
    
        self.update()

    def update(self):
        self.screen.blit(self.dial, (DIAL_POS))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)



def main():
    
    # center window on monitor
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    instr1, instr2 = instruction()

    instrument = Instrument(screen)
    
    # make mouse pointer invisible
    pygame.mouse.set_visible(False)
    
    # set at 0 position
    currentAngle = 270
    
    while True:
        requestedAngle = scan_keyboard(currentAngle)
        currentAngle   = requestedAngle

        screen.fill(STEEL)
        instrument.rotate(currentAngle)
    
        # draw help line for test purpose
        #help_lines(screen)
    
        # draw a black middle circle at needle
        pygame.draw.circle(screen, BLACK, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 23, 0)
        pygame.draw.circle(screen, WHITE, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 5, 0)

        # print out instruction
        screen.blit(instr1, (20, 500))
        screen.blit(instr2, (20, 530))
    
        pygame.display.update()


if __name__ == '__main__':
    main()
