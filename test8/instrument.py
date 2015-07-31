import numpy as np
import pygame
import pygame.locals
import sys
import math

xPos = 210
yPos = 300

# import all defines
from defines import *


class Instrument:
    """
    A class for handling the instrument.
    """
    def __init__(self, screen, image, middlePoint, instrumentIndex, speed, scale=IMAGE_SCALE):
        """
        input parameters:
          screen          -  Current surface name
          image           -  Image of needle
          middlePoint     -  Middle point of instrument
          instrumentIndex -  Index number of current instrument
          speed           -  Speed of needle
        """
        self.screen              = screen
        self.needleImage         = pygame.image.load(image).convert_alpha()
        self.instrumentMidPoint  = middlePoint
        self.instrumentIndex     = instrumentIndex
        self.speed               = speed
        self.angle               = 0
        self.rpm                 = 0                      # number of rpm, used for test purpose
        self.mousePressed        = False                  # flag indicating when mouse is pressed
        self.scale               = scale                  # set scale of needle, default = IMAGE_SCALE

    def reset_parameters(self):
        """
        Reset needle.
        """
        self.angle         = 0
        self.rpm           = 0  
        self.mousePressed  = False

    def set_flag(self, flag):
        """
        Set flag to indicate whether the mouse was pressed or not.
        """
        self.mousePressed = flag

    def set_needle_position(self, angle):
            self.angle = angle

    def rotate(self, rotation):
        """
        Rotates and re-centers the leftInstrument.
        """

        # if mouse button pressed then rotate leftInstrument
        if self.mousePressed:

            # increment loop counter, used for debug purpose
            self.rpm += 1

            # rotate instrument counter clock wise
            if int(self.angle) < rotation:
                if (abs(self.angle-rotation) < TEST_ROT_SPEED):
                    self.angle += 1
                self.angle += self.speed

            # rotate instrument clock wise
            elif int(self.angle) > rotation:
                if (abs(self.angle-rotation) > TEST_ROT_SPEED):
                    self.angle -= 1
                self.angle -= self.speed

            else:
                print 'Stopped'

            # clear flag when instrument has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False

        # rotate needle
        self.image = pygame.transform.rotate(self.needleImage, self.angle)

        # reset the center
        self.rect = self.image.get_rect()

    def blit_needle(self):
        self.screen.blit(self.image, self.rect)

    def instrument_update(self, degAngle):
        """
        """
        self.rotate(degAngle)

        self.rect.center = self.instrumentMidPoint
        print 'Angle:',self.angle,'   -  Midpoint Rect:',self.rect
        self.rect.center += np.array([np.cos(math.radians(self.angle)) * OFFSET_X,
                                      -np.sin(math.radians(self.angle)) * OFFSET_Y])
        print 'Rect:',self.rect

        self.blit_needle()

