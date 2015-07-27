import numpy as np
import pygame
import pygame.locals
import sys
import math

# import all defines
from defines import *

class Instrument:
    """
    A class for handling instruments and its needle.
    """
    def __init__(self, image, rotationSpeed):
        """
        Constructor.
        """
        self.base = pygame.image.load(image)

        self.speed        = rotationSpeed  # rotation speed of instrument
        self.angle        = 0              # current angle in radians
        self.rpm          = 0              # number of rpm, used for test purpose
        self.mousePressed = False          # flag indicating when mouse is pressed

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

    def rot(self, needleImage, needleRect, displayMidPoint, offset1, offset2):
        needleRect.center += np.asarray(displayMidPoint)
        needleRect.center += np.array([np.cos(math.radians(self.angle)) * offset1,
                                      -np.sin(math.radians(self.angle)) * offset2])

    def set_needle_position(self, angle):
            self.angle = angle
            self.image = pygame.transform.rotozoom(self.base, self.angle, IMAGE_SCALE)
            self.rect = self.image.get_rect()
            self.rect.center = (0, 0)
            return self.image, self.rect

    def rotate(self, rotation):
        """
        Rotates and re-centers the leftInstrument.
        """

        # if mouse button pressed then rotate leftInstrument
        if self.mousePressed:

            # increment loop counter, used for debug purpose
            self.rpm += 1

            # rotate leftInstrument counter clock wise
            if int(self.angle) < rotation:
                self.angle += self.speed

            # rotate leftInstrument clock wise
            elif int(self.angle) > rotation:
                self.angle -= self.speed

            else:
                print 'Stopped'

            # clear flag when leftInstrument has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False

        # rotate needle
        image = pygame.transform.rotozoom(self.base, self.angle, IMAGE_SCALE)

        # reset the center
        rect = image.get_rect()
        rect.center = (0, 0)
 
        return image, rect

    def blit_needle(self, scr, needleImage, needleRect):
        scr.blit(needleImage, needleRect)

