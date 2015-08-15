# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : flight_instr.py
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
       scan_keyboard.inputData1 = 30

   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
           pygame.quit()
           sys.exit()

       elif event.type == KEYDOWN and event.key == pygame.K_0:
           scan_keyboard.inputData1 = 130

       elif event.type == KEYDOWN and event.key == pygame.K_1:
           scan_keyboard.inputData1 = 30

       elif event.type == KEYDOWN and event.key == pygame.K_2:
           scan_keyboard.inputData1 = 40

       elif event.type == KEYDOWN and event.key == pygame.K_3:
           scan_keyboard.inputData1 = 50

       elif event.type == KEYDOWN and event.key == pygame.K_4:
           scan_keyboard.inputData1 = 60

       elif event.type == KEYDOWN and event.key == pygame.K_5:
           scan_keyboard.inputData1 = 70

       elif event.type == KEYDOWN and event.key == pygame.K_6:
           scan_keyboard.inputData1 = 80

       elif event.type == KEYDOWN and event.key == pygame.K_7:
           scan_keyboard.inputData1 = 90

       elif event.type == KEYDOWN and event.key == pygame.K_8:
           scan_keyboard.inputData1 = 100

       elif event.type == KEYDOWN and event.key == pygame.K_9:
           scan_keyboard.inputData1 = 10

       elif event.type == KEYDOWN and event.key == pygame.K_q:
           scan_keyboard.inputData1 = -40

   return scan_keyboard.inputData1


class AirSpeedInstrument():
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
        self.dial          = pygame.image.load('airspeed2.png')
        #self.needle        = pygame.image.load('white_needle.png')
        self.needle        = pygame.image.load('airspeed_needle2.png')
        self.nail          = pygame.image.load('grey_nail.png')

        self.dialRectangle  = self.dial.get_rect().size
        print 'Size of Airspeed image:',self.dialRectangle
        self.nailRectangle  = self.nail.get_rect().size
        print 'Size of Nail image:',self.nailRectangle

        self.reduceSpeedHiLo = 0.0         # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0         # reduce needle speed from lo to hi
        self.requestedAngle  = 0           # requested angle from user
        self.currentAngle    = startAngle  # current angle of needle
        self.finalAngle      = 0           # final angle that was requested
        self.flag1           = False       # flag to handle overshoot of needle
        self.flag2           = False       # flag to handle overshoot of needle
        self.inputData       = 0.0         # input data

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data. N.B! Since the scale is 
       not linear from 0 - 100 we need to split the calculation. Under the value 55 or above.
       Input:
         inputData - Input value. Between 0 - 100.
       """
       self.inputData = inputData
       requestedAngle  = int(-1.5*inputData + 118)

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

        self.rotatedNail = pygame.transform.rotate(self.nail, angle)
        self.rotatedNailRectangle = self.rotatedNail.get_rect()

        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (self.needlePos)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * NEEDLE_OFFSET_X,
                                            -np.sin(math.radians(angle)) * NEEDLE_OFFSET_Y])

        self.rotatedNailRectangle.center = (self.needlePos)
        self.rotatedNailRectangle.center += np.array([np.cos(math.radians(angle)) * 0,
                                            -np.sin(math.radians(angle)) * 0])


        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and input data value
        """
        self.screen.blit(self.dial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)
#        self.screen.blit(self.rotatedNail, self.rotatedNailRectangle)

       # draw circle at needle
       # pygame.draw.circle(self.screen, GREY, (self.needlePos), 14, 0)
       # pygame.draw.circle(self.screen, BLACK,  (self.needlePos), 3,  0)

class AltimeterInstrument():
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
        self.dial          = pygame.image.load('altimeter.png')
        self.needle        = pygame.image.load('needle_long.png')

        self.reduceSpeedHiLo = 0.0         # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0         # reduce needle speed from lo to hi
        self.requestedAngle  = 0           # requested angle from user
        self.currentAngle    = startAngle  # current angle of needle
        self.finalAngle      = 0           # final angle that was requested
        self.flag1           = False       # flag to handle overshoot of needle
        self.flag2           = False       # flag to handle overshoot of needle
        self.inputData       = 0.0         # input data

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data. N.B! Since the scale is 
       not linear from 0 - 100 we need to split the calculation. Under the value 55 or above.
       Input:
         inputData - Input value. Between 0 - 100.
       """
       self.inputData = inputData
       requestedAngle  = int(-1.5*inputData + 118)

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
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * NEEDLE_OFFSET_X,
                                            -np.sin(math.radians(angle)) * NEEDLE_OFFSET_Y])

        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and input data value
        """
        self.screen.blit(self.dial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)

def main():
    
    # center window on monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(10,10)

    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption(85*' '+'--- HzFlyer Flight Instruments ---')

    startAngle = 180 # start angle of needle
    airSpeedNeedleSpeed = 1.0 # rotation speed for needle, instrument1

    screen = pygame.display.set_mode((WIDTH-400, HEIGHT), 0, 32)

    # create instrument instance
    airSpeedInstrument = AirSpeedInstrument(screen, 
                                            startAngle, 
                                            SPEEDO_DIAL_POS_INSTR1, 
                                            SPEEDO_NEEDLE_POS_INSTR1,
                                            airSpeedNeedleSpeed, 
                                            INSTRUMENT1)

    altimeterInstrument = AltimeterInstrument(screen, 
                                              startAngle, 
                                              SPEEDO_DIAL_POS_INSTR2, 
                                              SPEEDO_NEEDLE_POS_INSTR2,
                                              airSpeedNeedleSpeed, 
                                              INSTRUMENT2)
    
    while True:

        screen.fill(BLACK)

        # scan keyboard to get an input value and send it to the instrument
        data1 = scan_keyboard()
        airSpeedInstrument.input_data(data1)
#        altimeterInstrument.input_data(data1)

        pygame.draw.line(screen, WHITE, (30,200),(500,200) , 1)  # horizontal line
        pygame.draw.line(screen, WHITE, (200,40),(200,500) , 1)  # vertical line

        # now, get everything visible on the screen
        #pygame.display.update()
        pygame.display.flip()
        fpsClock.tick(30)

if __name__ == '__main__':
    main()
