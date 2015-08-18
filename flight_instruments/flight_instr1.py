# Auther      : Heinz Samuelsson
# Date        : 2015-08-02
# File        : flight_instr1.py
# Reference   : -
# Description : Flight instruments are simulated.
#
# Python ver : 2.7.3 (gcc 4.6.3)

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


def draw_help_lines(screen):
    """
    Draw help lines to show center position.
    Input:
      screen - Current defined screen.
    """
    # horizontal line
    pygame.draw.line(screen, WHITE, 
                    (X_INDENT_LINE, SIZE_OF_INSTRUMENT_1[0]/2 + DIAL_POS_INSTR1[1]),
                    (WIDTH-X_INDENT_LINE, SIZE_OF_INSTRUMENT_1[0]/2 + DIAL_POS_INSTR1[1]),
                     1)

    pygame.draw.line(screen, WHITE, 
                    (X_INDENT_LINE, SIZE_OF_INSTRUMENT_2[0]/2 + DIAL_POS_INSTR2[1]),
                    (WIDTH-X_INDENT_LINE, SIZE_OF_INSTRUMENT_2[0]/2 + DIAL_POS_INSTR2[1]),
                     1)

    # vertical line
    pygame.draw.line(screen, WHITE, 
                     (SIZE_OF_INSTRUMENT_1[0]/2 + DIAL_POS_INSTR1[0], X_INDENT_LINE),
                     (SIZE_OF_INSTRUMENT_1[0]/2 + DIAL_POS_INSTR1[0], HEIGHT-X_INDENT_LINE),
                      1)

    pygame.draw.line(screen, WHITE, 
                     (SIZE_OF_INSTRUMENT_2[0]/2 + DIAL_POS_INSTR2[0], X_INDENT_LINE),
                     (SIZE_OF_INSTRUMENT_2[0]/2 + DIAL_POS_INSTR2[0], HEIGHT-X_INDENT_LINE),
                      1)


class Instrument():
    def __init__(self, screen, dialName, needleName, startAngle, dialPos, needlePos, needleOffset):
        """
        Define input parameters and load images of dial and needle.
        Input:
          screen        - Current defined screen.
          dialName      - Name of the dial.
          needleName    - Name of the needle.
          startAngle    - Start angle for needle.
          dialPos       - Position of dial.
          needlePos     - Position of needle.
          needleOffset  - Offset position for needle, this is setting the rotation point
        """
        self.screen        = screen
        self.dialPos       = dialPos
        self.needlePos     = needlePos
        self.speed         = SPEED_OF_NEEDLE 
        self.dial          = pygame.image.load(dialName)
        self.needle        = pygame.image.load(needleName)
        self.nail          = pygame.image.load('grey_nail.png')
        self.needleOffset  = needleOffset

        self.requestedAngle  = 0           # requested angle from user
        self.currentAngle    = startAngle  # current angle of needle
        self.finalAngle      = 0           # final angle that was requested
        self.flag1           = False       # flag to handle overshoot of needle
        self.flag2           = False       # flag to handle overshoot of needle
        self.inputData       = 0.0         # input data

        self._get_rect_size()

    def _get_rect_size(self):
        self.dialRect   = self.dial.get_rect()
        self.needleRect = self.needle.get_rect()
        print 'Dial rectangle:  ',self.dialRect
        print 'Needle rectangle:',self.needleRect

    def input_data(self, inputData):
       #"""
       # User must implement its own calculation of the angle for each instrument.
       #"""
       pass

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
        self.rotatedImage = pygame.transform.rotozoom(self.needle, angle, 1.0)
        self.rotatedImageRectangle = self.rotatedImage.get_rect()

        # compensate for rotation of needle
        self.rotatedImageRectangle.center = (self.needlePos)
        self.rotatedImageRectangle.center += np.array([np.cos(math.radians(angle)) * self.needleOffset[0],
                                            -np.sin(math.radians(angle)) * self.needleOffset[1]])

        # blit images
        self._blit_images()

    def _blit_images(self): 
        """ 
        Blit dials, needle and input data value
        """
        self.screen.blit(self.dial, (self.dialPos))
        self.screen.blit(self.rotatedImage, self.rotatedImageRectangle)


class AirSpeedInstrument(Instrument):
    def __init__(self, screen, dialName, needleName, startAngle, dialPos, needlePos, needleOffset):
        Instrument.__init__(self, screen, dialName, needleName, startAngle, dialPos, needlePos, needleOffset)

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data.
       Input:
         inputData - Input data value.
       """
       self.inputData = inputData
       requestedAngle  = int(-1.5*inputData + 118)

       self.input_angle(requestedAngle)


class AltimeterInstrument(Instrument):
    def __init__(self, screen, dialName, needleName, startAngle, dialPos, needlePos, needleOffset):
        Instrument.__init__(self, screen, dialName, needleName, startAngle, dialPos, needlePos, needleOffset)

    def input_data(self, inputData):
       """
       Calculate the angle with respect to the input data.
       Input:
         inputData - Input data value.
       """
       self.inputData = inputData
       requestedAngle  = int(-2.5*inputData + 118)

       self.input_angle(requestedAngle)


# --------------------------------------------------------------------------------- 
#  Main
# --------------------------------------------------------------------------------- 
def main(argv):
 
    test = False

    # argv - hidden argument used for test purpose
    # 1 => draw help lines at instrument to find center point
    if len(argv) > 0:
        test = True
 
    # position window on monitor
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(WINDOW_POS)

    pygame.init()
    fpsClock = pygame.time.Clock()

    background = pygame.image.load('background.png')
    pygame.display.set_caption(120*' '+'--- HzFlyer Flight Instruments ---')
    startAngle = 180 # start angle of needle
    screen = pygame.display.set_mode((WIDTH, HEIGHT), WINDOW_STYLE, COLOR_DEPTH)

    # create instrument instance
    airSpeedInstrument = AirSpeedInstrument(screen, 
                                            'airspeed2.png',
                                            'airspeed_needle2.png',
                                            startAngle, 
                                            DIAL_POS_INSTR1,
                                            NEEDLE_POS_INSTR1,
                                            NEEDLE_OFFSET_INSTR1
                                            )

    altimeterInstrument = AltimeterInstrument(screen, 
                                              'airspeed2.png',
                                              'needle_long.png',
                                              startAngle, 
                                              DIAL_POS_INSTR2,
                                              NEEDLE_POS_INSTR2,
                                              NEEDLE_OFFSET_INSTR2
                                              )
    
    while True:

        screen.blit(background, SCREEN_ORIGO)

        # scan keyboard to get an input value and send it to the instrument
        inputData = scan_keyboard()
        airSpeedInstrument.input_data(inputData)
        altimeterInstrument.input_data(inputData)

        if test:
            draw_help_lines(screen)

        # now, get everything visible on the screen
        pygame.display.flip()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main(sys.argv[1:])

#----------------------------------------------------------------------------------------------------------
# End of File
#----------------------------------------------------------------------------------------------------------
