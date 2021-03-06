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
    inputString = inputValueFont.render("Input data: ", 0, WHITE)

    inputValue1 = inputValueFont.render(str(value), 0, WHITE)
    inputValue2 = inputValueFont.render(str(value2), 0, WHITE)
    inputValue3 = inputValueFont.render(str(value3), 0, WHITE)

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
           scan_keyboard.inputData1 = 1
           scan_keyboard.inputData2 = 2
           scan_keyboard.inputData3 = 3

       elif event.type == KEYDOWN and event.key == pygame.K_2:
           scan_keyboard.inputData1 = 2
           scan_keyboard.inputData2 = 3
           scan_keyboard.inputData3 = 4

       elif event.type == KEYDOWN and event.key == pygame.K_3:
           scan_keyboard.inputData1 = 3
           scan_keyboard.inputData2 = 4
           scan_keyboard.inputData3 = 5

       elif event.type == KEYDOWN and event.key == pygame.K_4:
           scan_keyboard.inputData1 = 4
           scan_keyboard.inputData2 = 5
           scan_keyboard.inputData3 = 6

       elif event.type == KEYDOWN and event.key == pygame.K_5:
           scan_keyboard.inputData1 = 5
           scan_keyboard.inputData2 = 6
           scan_keyboard.inputData3 = 7

       elif event.type == KEYDOWN and event.key == pygame.K_6:
           scan_keyboard.inputData1 = 6
           scan_keyboard.inputData2 = 7
           scan_keyboard.inputData3 = 8

       elif event.type == KEYDOWN and event.key == pygame.K_7:
           scan_keyboard.inputData1 = 7
           scan_keyboard.inputData2 = 8
           scan_keyboard.inputData3 = 9

       elif event.type == KEYDOWN and event.key == pygame.K_8:
           scan_keyboard.inputData1 = 8
           scan_keyboard.inputData2 = 9
           scan_keyboard.inputData3 = 0

       elif event.type == KEYDOWN and event.key == pygame.K_9:
           scan_keyboard.inputData1 = 9
           scan_keyboard.inputData2 = 1
           scan_keyboard.inputData3 = 2


   return scan_keyboard.inputData1, scan_keyboard.inputData2, scan_keyboard.inputData3


class Temp_Instrument():
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
        self.tempDial      = pygame.image.load('temp1.png')
        self.needle        = pygame.image.load('needle_long.png')

        self.reduceSpeedHiLo = 0.0   # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0   # reduce needle speed from lo to hi
        self.requestedAngle  = 0     # requested angle from user
        self.currentAngle    = startAngle   # current angle of needle
        self.finalAngle      = 0     # final angle that was requested
        self.flag1           = False # flag to handle overshoot of needle
        self.flag2           = False # flag to handle overshoot of needle

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data. N.B! Since the scale is 
       not linear from 0 - 100 we need to split the calculation. Under the value 55 or above.
       Input:
         inputData - Input value. Between 0 - 100.
       """
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
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * SPEEDO_OFFSET_X,
                                            -np.sin(math.radians(angle)) * SPEEDO_OFFSET_Y])
    
        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and draw center dot for the instrument.
        """
        self.screen.blit(self.tempDial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)

        # draw circle at needle
        #pygame.draw.circle(self.screen, LIGHT_GREY, (self.needlePos), 25, 0)
        #pygame.draw.circle(self.screen, BLACK,  (self.needlePos), 3,  0)


class Fuel_Instrument():
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
        self.fuelDial      = pygame.image.load('fuel.png')
        self.needle        = pygame.image.load('needle_long.png')

        self.reduceSpeedHiLo = 0.0   # reduce needle speed from hi to lo
        self.reduceSpeedLoHi = 0.0   # reduce needle speed from lo to hi
        self.requestedAngle  = 0     # requested angle from user
        self.currentAngle    = startAngle   # current angle of needle
        self.finalAngle      = 0     # final angle that was requested
        self.flag1           = False # flag to handle overshoot of needle
        self.flag2           = False # flag to handle overshoot of needle

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data. N.B! Since the scale is 
       not linear from 0 - 100 we need to split the calculation. Under the value 55 or above.
       Input:
         inputData - Input value. Between 0 - 100.
       """
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
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * SPEEDO_OFFSET_X,
                                            -np.sin(math.radians(angle)) * SPEEDO_OFFSET_Y])
    
        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and draw center dot for the instrument.
        """
        self.screen.blit(self.fuelDial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)

        # draw circle at needle
        #pygame.draw.circle(self.screen, LIGHT_GREY, (self.needlePos), 25, 0)
        #pygame.draw.circle(self.screen, BLACK,  (self.needlePos), 3,  0)


def main(argv):
    
    # center window on monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(10,10)

    pygame.init()
    fpsClock = pygame.time.Clock()
    pygame.display.set_caption('Instrument')

    breakFont = pygame.font.SysFont("None",28)
    startBreak = breakFont.render("Break", 0, BLACK)

    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    instr1 = instruction()

    # create instrument instances
    instrument1 = Temp_Instrument(screen, 180, SPEEDO_DIAL_POS_INSTR1, SPEEDO_NEEDLE_POS_INSTR1, 1.0, INSTRUMENT1)
    instrument2 = Fuel_Instrument(screen, 180, SPEEDO_DIAL_POS_INSTR2, SPEEDO_NEEDLE_POS_INSTR2, 2.0, INSTRUMENT2)
    instrument3 = Temp_Instrument(screen, 180, SPEEDO_DIAL_POS_INSTR3, SPEEDO_NEEDLE_POS_INSTR3, 3.0, INSTRUMENT3)
    
    # make mouse pointer invisible
    #pygame.mouse.set_visible(False)
    
    while True:

        screen.fill(BLACK)

        # scan keyboard to get an input value and send it to the instrument
        data1, data2, data3 = scan_keyboard()
        instrument1.input_data(data1)
        instrument2.input_data(data2)
        instrument3.input_data(data3)

        # print out instruction
        screen.blit(instr1, (20, 530))
        print_input_value_on_screen(screen, data1, data2, data3)
    
        # now, get everything visible on the screen
        #pygame.draw.line(screen, RED, (94,30), (94, 300))
        #pygame.draw.line(screen, RED, (394,30), (394, 300))
        #pygame.draw.line(screen, RED, (244,30), (244, 300))
        #pygame.draw.line(screen, RED, (40,250), (420, 250))
        pygame.display.update()
        fpsClock.tick(30)


if __name__ == '__main__':
    main(sys.argv[1:])
