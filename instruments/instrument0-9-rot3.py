# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : instrument0-9_rot3.py
# Reference   : -
# Description : Instrument is showing different values depending on the input value.
#               The values are set by key 0-9 or q/w/e/r/t/y.
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


def instruction():
    """
    Print out instructions.
    """
    instructionFont = pygame.font.SysFont("None",28)
    instr1 = instructionFont.render("Use keys 0 - 9 or q/w/e/r/t/y to change instrument readings", 0, BLACK)
    return instr1


def input_value(screen, value):
    """
    Print out current input value on the screen.
    """
    inputValueFont = pygame.font.SysFont("None",28)
    inputString = inputValueFont.render("Input data: ", 0, BLACK)
    inputValue = inputValueFont.render(str(value), 0, BLACK)
    screen.blit(inputString, (20, 30))
    screen.blit(inputValue, (130, 30))


def scan_keyboard():
   """
   Scan keyboard and set requested angle.
   Escape key          => application quit
   key  0-9 or qwerty  => Change instrument reading
   """
   requestedAngle = 0

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

       elif event.type == KEYDOWN and event.key == pygame.K_0:
           scan_keyboard.inputData = 0

       elif event.type == KEYDOWN and event.key == pygame.K_1:
           scan_keyboard.inputData = 1

       elif event.type == KEYDOWN and event.key == pygame.K_2:
           scan_keyboard.inputData = 2

       elif event.type == KEYDOWN and event.key == pygame.K_3:
           scan_keyboard.inputData = 3

       elif event.type == KEYDOWN and event.key == pygame.K_4:
           scan_keyboard.inputData = 4

       elif event.type == KEYDOWN and event.key == pygame.K_5:
           scan_keyboard.inputData = 5

       elif event.type == KEYDOWN and event.key == pygame.K_6:
           scan_keyboard.inputData = 6

       elif event.type == KEYDOWN and event.key == pygame.K_7:
           scan_keyboard.inputData = 7

       elif event.type == KEYDOWN and event.key == pygame.K_8:
           scan_keyboard.inputData = 8

       elif event.type == KEYDOWN and event.key == pygame.K_9:
           scan_keyboard.inputData = 9

       elif event.type == KEYDOWN and event.key == pygame.K_q:
           scan_keyboard.inputData = 1.3

       elif event.type == KEYDOWN and event.key == pygame.K_w:
           scan_keyboard.inputData = 5.7

       elif event.type == KEYDOWN and event.key == pygame.K_e:
           scan_keyboard.inputData = 8.1

       elif event.type == KEYDOWN and event.key == pygame.K_r:
           scan_keyboard.inputData = 4.7

       elif event.type == KEYDOWN and event.key == pygame.K_t:
           scan_keyboard.inputData = 4.8

       elif event.type == KEYDOWN and event.key == pygame.K_y:
           scan_keyboard.inputData = 4.9

   # calculate angle of needle, 270 degrees => '0'
   requestedAngle = int(-36*scan_keyboard.inputData + 270)
   return requestedAngle, scan_keyboard.inputData


class Instrument():
    def __init__(self, screen):
        """
        Define current screen and load images of dial and needle.
        Input:
          screen  - Current defined screen.
        """
        self.screen = screen
        self.dial = pygame.image.load('instrument0-9.png')
        self.needle = pygame.image.load('needle2.png')

    def rotate(self, angle):
        """
        Rotate needle and reposition the needle due to the angle.
        Input:
          angle - The rotation angle for the needle.
        """
        self.rotatedImage = pygame.transform.rotate(self.needle, angle)
        self.rotatedImageRectangle = self.rotatedImage.get_rect()
    
        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (NEEDLE_POS)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * OFFSET_X,
                                            -np.sin(math.radians(angle)) * OFFSET_Y])
    
        # blit instrument
        self.update()

    def update(self):
        """
        Blit dial and needle on the screen.
        """
        self.screen.blit(self.dial, (DIAL_POS))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)



def main():
    
    # center window on monitor
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    fpsClock = pygame.time.Clock()

    breakFont = pygame.font.SysFont("None",28)
    startBreak = breakFont.render("Break", 0, BLACK)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    instr1 = instruction()

    # create instrument instance
    instrument = Instrument(screen)
    
    # make mouse pointer invisible
    pygame.mouse.set_visible(False)
    
    # set instrument at 0 position
    currentAngle = 270

    reduceSpeedHiLo = 0.0  # reduce needle speed from hi to lo
    reduceSpeedLoHi = 0.0  # reduce needle speed from lo to hi
    speed           = 1.0  # needle speed
    previousValue   = 0.0  # temp variable to hold previous value
    
    while True:

        screen.fill(STEEL)

        # scan keyboard to get an input value also check if the new value differs
        # from the previous one. If so then reset the reduce speed variables
        requestedAngle, data = scan_keyboard()
        input_value(screen, data)

        if previousValue != requestedAngle:
            print '*'*20
            print '***  New request  ***'
            print '*'*20
            reduceSpeedHiLo = 0.0
            reduceSpeedLoHi = 0.0

        previousValue = requestedAngle

        # rotate from low to hi
        if requestedAngle < currentAngle:
            print 'Low->Hi  -  Requested angle:',requestedAngle,'  -  Current angle:',currentAngle,

            currentAngle -= speed - reduceSpeedLoHi

            diff = requestedAngle - currentAngle
            print '  -  Diff:',diff            

            if currentAngle == requestedAngle or ((requestedAngle - currentAngle) > 0):
                print 'Low->Hi stopped'
                currentAngle = requestedAngle
                reduceSpeedLoHi = 0.0
                reduceSpeedHiLo = 0.0

            # start to slow down needle
            if (requestedAngle - currentAngle) > -45:
                screen.blit(startBreak, (20, 560))
                reduceSpeedLoHi += 0.01

            instrument.rotate(currentAngle)

        # rotate from hi to low
        elif requestedAngle > currentAngle:
            print 'Hi->Low  -  Requested angle:',requestedAngle,'  -  Current angle:',currentAngle,

            currentAngle += speed - reduceSpeedHiLo

            diff = requestedAngle - currentAngle
            print '  -  Diff:',diff            

            if currentAngle == requestedAngle or ((requestedAngle - currentAngle) < 0):
                print 'Hi->Low stopped'
                currentAngle = requestedAngle
                reduceSpeedHiLo = 0.0
                reduceSpeedLoHi = 0.0

            # start to slow down needle
            if (requestedAngle - currentAngle) < 45:
                screen.blit(startBreak, (20, 560))
                reduceSpeedHiLo += 0.01

            instrument.rotate(currentAngle)

        else:
            instrument.rotate(requestedAngle)
     
        # draw a black middle circle at needle
        pygame.draw.circle(screen, BLACK, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 23, 0)
        pygame.draw.circle(screen, WHITE, (X_NEEDLE_COORD,Y_NEEDLE_COORD), 5, 0)

        # print out instruction
        screen.blit(instr1, (20, 530))
    
        pygame.display.update()
        fpsClock.tick(30)


if __name__ == '__main__':
    main()
