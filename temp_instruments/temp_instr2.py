# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : speedo.py
# Reference   : -
# Description : Two different instruments are loaded.
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

       elif event.type == KEYDOWN and event.key == pygame.K_1:
           scan_keyboard.inputData1 = 1
           scan_keyboard.inputData2 = 7.7

       elif event.type == KEYDOWN and event.key == pygame.K_2:
           scan_keyboard.inputData1 = 3
           scan_keyboard.inputData2 = 8.4

       elif event.type == KEYDOWN and event.key == pygame.K_3:
           scan_keyboard.inputData1 = 3.4
           scan_keyboard.inputData2 = 4

       elif event.type == KEYDOWN and event.key == pygame.K_4:
           scan_keyboard.inputData1 = 4
           scan_keyboard.inputData2 = 4

       elif event.type == KEYDOWN and event.key == pygame.K_5:
           scan_keyboard.inputData1 = 6.1
           scan_keyboard.inputData2 = 5.5

       elif event.type == KEYDOWN and event.key == pygame.K_6:
           scan_keyboard.inputData1 = 6.3
           scan_keyboard.inputData2 = 2

       elif event.type == KEYDOWN and event.key == pygame.K_7:
           scan_keyboard.inputData1 = 6
           scan_keyboard.inputData2 = 6.5

       elif event.type == KEYDOWN and event.key == pygame.K_8:
           scan_keyboard.inputData1 = 8
           scan_keyboard.inputData2 = 9

       elif event.type == KEYDOWN and event.key == pygame.K_9:
           scan_keyboard.inputData1 = 9
           scan_keyboard.inputData2 = 1


   return scan_keyboard.inputData1, scan_keyboard.inputData2


class Instrument_1():
    def __init__(self, screen, startAngle, dialPos, needlePos, speed, instrumentNo):
        """
        Define input parameters and load images of dial and needle.
        Input:
          screen        - Current defined screen.
          startAngle    - Start angle for needle.
          dialPos       - Position of dial.
          needlePos     - Position of needle.
          speed         - Rotation speed of needle.
          instrumentNo  - Instrument number.
        """
        self.screen        = screen
        self.startAngle    = startAngle
        self.dialPos       = dialPos
        self.needlePos     = needlePos
        self.instrumentNo  = instrumentNo
        self.speed         = speed
        self.tempDial      = pygame.image.load('instrument1.png')
        self.needle        = pygame.image.load('red_needle_instr1.png')

        self.reduceSpeedHiLo = 0.0         # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0         # reduce needle speed from lo to hi
        self.requestedAngle  = 0           # requested angle from user
        self.currentAngle    = startAngle  # current angle of needle
        self.finalAngle      = 0           # final angle that was requested
        self.flag1           = False       # flag to handle overshoot of needle
        self.flag2           = False       # flag to handle overshoot of needle
        self.inputData       = 0.0         # input data
        self.inputValFont    = pygame.font.SysFont("None",38)

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data. N.B! Since the scale is 
       not linear from 0 - 100 we need to split the calculation. Under the value 55 or above.
       Input:
         inputData - Input value. Between 0 - 100.
       """
       self.inputData = inputData
       requestedAngle  = int(-20*inputData + 180)

       self.input_angle(requestedAngle)

    def input_angle(self, reqAngle):
        """
        Increment/decrement the angle until the requested angle is reached.
        Input:
          reqAngle - Requested angle in degrees.
        """
        # clear flags when new data arrives
        if self.finalAngle != reqAngle:
            self.flag1 = False
            self.flag2 = False

        if reqAngle < self.currentAngle and not self.flag2:
            #print '[1] Requested angle:',reqAngle,'  -  Current angle:',self.currentAngle
            self.currentAngle -= self.speed
            self.flag1 = True

        elif reqAngle > self.currentAngle and not self.flag1:
            #print '[2] Requested angle:',reqAngle,'  -  Current angle:',self.currentAngle
            self.currentAngle += self.speed
            self.flag2 = True

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
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * INSTR2_OFFSET_X,
                                            -np.sin(math.radians(angle)) * INSTR2_OFFSET_Y])
    
        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and input data value
        """
        self.screen.blit(self.tempDial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)
        inputValue = self.inputValFont.render(str(self.inputData), 0 , BLACK)
        self.screen.blit(inputValue, (self.needlePos[0]-10,197))


def main():
    
    # center window on monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(10,10)

    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Instrument')

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    # create instrument instances
    instrument1 = Instrument_1(screen, 180, SPEEDO_DIAL_POS_INSTR1, SPEEDO_NEEDLE_POS_INSTR1, 1.0, INSTRUMENT1)
    instrument2 = Instrument_1(screen, 180, SPEEDO_DIAL_POS_INSTR2, SPEEDO_NEEDLE_POS_INSTR2, 2.0, INSTRUMENT2)
    
    while True:

        screen.fill((131,131,115))

        # scan keyboard to get an input value and send it to the instrument
        data1, data2 = scan_keyboard()
        instrument1.input_data(data1)
        instrument2.input_data(data2)

        # now, get everything visible on the screen
        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)


if __name__ == '__main__':
    main()
