# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : speedo.py
# Reference   : -
# Description : Instrument is showing different values depending on the input value.
#               The values are set by key 0-9 or q/w/e/r/t/y.
#               defines.py is used for a lot of defined constants.
#
# Python ver : 2.7.3 (gcc 4.6.3)

# Comments: Move blit of dial to __init__
# Comments: Move calc of angle to each instrument from scan key

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


def print_input_value_on_screen(screen, value, value2, value3):
    """
    Print out current input value on the screen.
    """
    inputValueFont = pygame.font.SysFont("None",28)
    inputString = inputValueFont.render("Input data: ", 0, BLACK)

    inputValue1 = inputValueFont.render(str(value), 0, BLACK)
    inputValue2 = inputValueFont.render(str(value2), 0, BLACK)
    inputValue3 = inputValueFont.render(str(value3), 0, BLACK)

    screen.blit(inputString, (SPEEDO_DIAL_POS_INSTR1[0]+50,  350))
    screen.blit(inputValue1, (SPEEDO_DIAL_POS_INSTR1[0]+160, 350))
    screen.blit(inputString, (SPEEDO_DIAL_POS_INSTR2[0]+50,  350))
    screen.blit(inputValue2, (SPEEDO_DIAL_POS_INSTR2[0]+160, 350))
    screen.blit(inputString, (SPEEDO_DIAL_POS_INSTR3[0]+50,  350))
    screen.blit(inputValue3, (SPEEDO_DIAL_POS_INSTR3[0]+160, 350))


def scan_keyboard():
   """
   Scan keyboard and set requested angle.
   Escape key          => application quit
   key  0-9 or qwerty  => Change instrument reading
   """
   requestedAngle = 0

   # static variable
   if not hasattr(scan_keyboard, "inputData1"):
       scan_keyboard.inputData1 = 0
   if not hasattr(scan_keyboard, "inputData2"):
       scan_keyboard.inputData2 = 0
   if not hasattr(scan_keyboard, "inputData3"):
       scan_keyboard.inputData3 = 0

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_0:
           scan_keyboard.inputData1 = 0
           scan_keyboard.inputData2 = 0
           scan_keyboard.inputData3 = 0

       elif event.type == KEYDOWN and event.key == pygame.K_1:
           scan_keyboard.inputData1 = 55
           scan_keyboard.inputData2 = 70
           scan_keyboard.inputData3 = 90

       elif event.type == KEYDOWN and event.key == pygame.K_2:
           scan_keyboard.inputData1 = 60
           scan_keyboard.inputData2 = 80
           scan_keyboard.inputData3 = 65

       elif event.type == KEYDOWN and event.key == pygame.K_3:
           scan_keyboard.inputData1 = 65
           scan_keyboard.inputData2 = 65
           scan_keyboard.inputData3 = 65

       elif event.type == KEYDOWN and event.key == pygame.K_4:
           scan_keyboard.inputData1 = 70
           scan_keyboard.inputData2 = 100
           scan_keyboard.inputData3 = 55

       elif event.type == KEYDOWN and event.key == pygame.K_5:
           scan_keyboard.inputData1 = 100
           scan_keyboard.inputData2 = 90
           scan_keyboard.inputData3 = 80

       elif event.type == KEYDOWN and event.key == pygame.K_6:
           scan_keyboard.inputData1 = 80
           scan_keyboard.inputData2 = 100
           scan_keyboard.inputData3 = 70

       elif event.type == KEYDOWN and event.key == pygame.K_7:
           scan_keyboard.inputData1 = 85
           scan_keyboard.inputData2 = 55
           scan_keyboard.inputData3 = 55

       elif event.type == KEYDOWN and event.key == pygame.K_8:
           scan_keyboard.inputData1 = 90
           scan_keyboard.inputData2 = 70
           scan_keyboard.inputData3 = 75

       elif event.type == KEYDOWN and event.key == pygame.K_9:
           scan_keyboard.inputData1 = 95
           scan_keyboard.inputData2 = 60
           scan_keyboard.inputData3 = 65

       elif event.type == KEYDOWN and event.key == pygame.K_q:
           scan_keyboard.inputData1 = 100

       elif event.type == KEYDOWN and event.key == pygame.K_w:
           scan_keyboard.inputData2 = 55

       elif event.type == KEYDOWN and event.key == pygame.K_e:
           scan_keyboard.inputData3 = 88

       elif event.type == KEYDOWN and event.key == pygame.K_r:
           scan_keyboard.inputData1 = 13 

       elif event.type == KEYDOWN and event.key == pygame.K_t:
           scan_keyboard.inputData2 = 42

       elif event.type == KEYDOWN and event.key == pygame.K_y:
           scan_keyboard.inputData3 = 36

   return scan_keyboard.inputData1, scan_keyboard.inputData2, scan_keyboard.inputData3


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
        self.dial   = pygame.image.load('speedo2.png')
        self.needle = pygame.image.load('needle3.png')

        self.speed           = 1.0  # needle speed
        self.reduceSpeedHiLo = 0.0  # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0  # reduce needle speed from lo to hi
        self.requestedAngle  = 0    # requested angle from user
        self.currentAngle    = 270  # current angle of needle
        self.finalAngle      = 0    # final angle that was requested

    def input_data(self, inputData):
       """
       Input data to instrument.
       Input:
         inputData - input data.
       """

       # since the scale is not linear from 0 - 100 we need to split the calculation
       if inputData > 55:
           requestedAngle  = int(-5.1*inputData + 472)
       else:
           requestedAngle  = int(-0.5*inputData + 220)

       self.input_angle(requestedAngle)

    def input_angle(self, reqAngle):
        """
        Increment/decrement the angle until the requested angle is reached.
        Input:
          reqAngle - requested angle in degrees.
        """
        if self.finalAngle != reqAngle:
            print 'New data sent to instrument: [%d]' %(self.instrumentNo)

        if reqAngle < self.currentAngle:
            self.currentAngle -= self.speed
        elif reqAngle > self.currentAngle:
            self.currentAngle += self.speed

        self.finalAngle = reqAngle
        self._rotate(self.currentAngle)

    def _rotate(self, angle):
        """
        Rotate needle and reposition the needle due to the angle.
        Input:
          angle - The rotation angle for the needle.
        """
        self.rotatedImage = pygame.transform.rotate(self.needle, angle)
        self.rotatedImageRectangle = self.rotatedImage.get_rect()
    
        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (self.needlePos)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * SPEEDO_OFFSET_X,
                                            -np.sin(math.radians(angle)) * SPEEDO_OFFSET_Y])
    
        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dial, needle and draw center dot for the instrument.
        """
        self.screen.blit(self.dial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)

        # draw circle at needle
        pygame.draw.circle(self.screen, GREY, (self.needlePos), 14, 0)
        pygame.draw.circle(self.screen, BLACK,  (self.needlePos), 3,  0)


def main():
    
    # center window on monitor
    #os.environ['SDL_VIDEO_CENTERED'] = '1'
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(10,10)

    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Instrument')

    breakFont = pygame.font.SysFont("None",28)
    startBreak = breakFont.render("Break", 0, BLACK)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    instr1 = instruction()

    # create instrument instances
    instrument1 = Instrument(screen, 220, SPEEDO_DIAL_POS_INSTR1, SPEEDO_NEEDLE_POS_INSTR1, INSTRUMENT1)
    instrument2 = Instrument(screen, 220, SPEEDO_DIAL_POS_INSTR2, SPEEDO_NEEDLE_POS_INSTR2, INSTRUMENT2)
    instrument3 = Instrument(screen, 220, SPEEDO_DIAL_POS_INSTR3, SPEEDO_NEEDLE_POS_INSTR3, INSTRUMENT3)
    
    # make mouse pointer invisible
    pygame.mouse.set_visible(False)
    
    while True:

        screen.fill(STEEL)

        # scan keyboard to get an input value and send it to the instrument
        data1, data2, data3 = scan_keyboard()
        instrument1.input_data(data1)
        instrument2.input_data(data2)
        instrument3.input_data(data3)

        # print out instruction
        screen.blit(instr1, (20, 530))
        print_input_value_on_screen(screen, data1, data2, data3)
    
        # now, get everything visible on the screen
        pygame.display.update()
        fpsClock.tick(30)


if __name__ == '__main__':
    main()
