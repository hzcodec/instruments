# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : instrument_class1.py
# Reference   : -
# Description : Instrument is showing different values depending on the input value.
#               The values are set by key 0-9 or q/w/e/r/t/y.
#               defines.py is used for a lot of defined constants.
#
# Python ver : 2.7.3 (gcc 4.6.3)

# Comments: Move blit of dial to __init__

import pygame
import sys
from pygame.locals import *
import numpy as np
import math
import os
from defines import *


def instruction():
    """
    Print out instructions.
    """
    instructionFont = pygame.font.SysFont("None",28)
    instr1 = instructionFont.render("Use keys 0 - 9 or q/w/e/r/t/y to change instrument readings", 0, BLACK)
    return instr1


def print_input_value_on_screen(screen, value):
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
    def __init__(self, screen, startAngle, dialPos, needlePos, instrumentNo):
        """
        Define input parameters and load images of dial and needle.
        Input:
          screen        - Current defined screen.
          startAngle    - Start angle for needle.
          dialPos       - Position of dial.
          needlePos     - Position of needle.
          instrumentNo  - Instrument number.
        """
        self.screen        = screen
        self.startAngle    = startAngle
        self.dialPos       = dialPos
        self.needlePos     = needlePos
        self.instrumentNo  = instrumentNo
        self.dial   = pygame.image.load('instrument0-9.png')
        self.needle = pygame.image.load('needle2.png')

        self.speed           = 1.0  # needle speed
        self.reduceSpeedHiLo = 0.0  # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0  # reduce needle speed from lo to hi
        self.requestedAngle  = 0    # requested angle from user
        self.currentAngle    = 270  # current angle of needle

    def input_angle(self, reqAngle):
        if self.currentAngle != reqAngle:
            print 'New angle requested from instrument: [%d]' %(self.instrumentNo)

        self.currentAngle = reqAngle
        self.requestedAngle = reqAngle
        self.rotate(self.requestedAngle)

    def rotate(self, angle):
        """
        Rotate needle and reposition the needle due to the angle.
        Input:
          angle - The rotation angle for the needle.
        """
        self.rotatedImage = pygame.transform.rotate(self.needle, angle)
        self.rotatedImageRectangle = self.rotatedImage.get_rect()
    
        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (self.needlePos)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * OFFSET_X,
                                            -np.sin(math.radians(angle)) * OFFSET_Y])
    
        # blit instrument
        self.blit_images()

    def blit_images(self): 
        """ 
        Blit dial and needle on the screen.
        """
        self.screen.blit(self.dial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)

        # draw a black middle circle at needle
        pygame.draw.circle(self.screen, BLACK, (self.needlePos), 23, 0)
        pygame.draw.circle(self.screen, GREY,  (self.needlePos), 5,  0)



def main():
    
    # center window on monitor
    #os.environ['SDL_VIDEO_CENTERED'] = '1'
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(10,10)

    pygame.init()
    fpsClock = pygame.time.Clock()

    breakFont = pygame.font.SysFont("None",28)
    startBreak = breakFont.render("Break", 0, BLACK)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    instr1 = instruction()

    # create instrument instances
    instrument1 = Instrument(screen, 270, DIAL_POS_INSTR1, NEEDLE_POS_INSTR1, INSTRUMENT1)
    instrument2 = Instrument(screen, 270, DIAL_POS_INSTR2, NEEDLE_POS_INSTR2, INSTRUMENT2)
    instrument3 = Instrument(screen, 270, DIAL_POS_INSTR3, NEEDLE_POS_INSTR3, INSTRUMENT3)
    
    # make mouse pointer invisible
    pygame.mouse.set_visible(False)
    
    reduceSpeedHiLo = 0.0  # reduce needle speed from hi to lo
    reduceSpeedLoHi = 0.0  # reduce needle speed from lo to hi
    speed           = 1.0  # needle speed
    previousValue   = 0.0  # temp variable to hold previous value
    
    while True:

        screen.fill(STEEL)

        # scan keyboard to get an input value also check if the new value differs
        # from the previous one. If so then reset the reduce speed variables
        requestedAngle, data = scan_keyboard()
        instrument1.input_angle(requestedAngle)
        instrument2.input_angle(requestedAngle)

#        if previousValue != requestedAngle:
#            print '*'*20
#            print '***  New request  ***'
#            print '*'*20
#            reduceSpeedHiLo = 0.0
#            reduceSpeedLoHi = 0.0
#
#        previousValue = requestedAngle
#
#        # rotate from low to hi
#        if requestedAngle < currentAngle,
#
#            currentAngle -= speed - reduceSpeedLoHi
#
#            diff = requestedAngle - currentAngle
#            print '  -  Diff:',diff            
#
#            if currentAngle == requestedAngle or ((requestedAngle - currentAngle) > 0):
#                print 'Low->Hi stopped'
#                currentAngle = requestedAngle
#                reduceSpeedLoHi = 0.0
#                reduceSpeedHiLo = 0.0
#
#            # start to slow down needle
#            if (requestedAngle - currentAngle) > -45:
#                screen.blit(startBreak, (20, 560))
#                reduceSpeedLoHi += 0.01
#
#            instrument1.rotate(currentAngle)
#
#        else:
#            instrument1.rotate(requestedAngle)
     
        # print out instruction
        screen.blit(instr1, (20, 530))
        print_input_value_on_screen(screen, data)
    
        pygame.display.update()
        fpsClock.tick(30)


if __name__ == '__main__':
    main()
