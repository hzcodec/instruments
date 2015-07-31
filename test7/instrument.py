import numpy as np
import pygame
import pygame.locals
import sys
import math

xPos = 210
yPos = 300

# import all defines
from tripple_defines import *

class Indicator:
    def __init__(self, screen):
        self.screen = screen
        self.turn_off_indicator()

    def turn_on_indicator(self, instNr):
        if instNr == 1:
            pygame.draw.circle(self.screen, RED, FIRST_INDICATOR_MID_POINT, INDICATOR-INDICATOR_THICKNESS, 0)
        elif instNr == 2:
            pygame.draw.circle(self.screen, BLUE, SECOND_INDICATOR_MID_POINT, INDICATOR-INDICATOR_THICKNESS, 0)
        elif instNr == 3:
            pygame.draw.circle(self.screen, GREEN, THIRD_INDICATOR_MID_POINT, INDICATOR-INDICATOR_THICKNESS, 0)
        elif instNr == 4:
            pygame.draw.circle(self.screen, YELLOW,  FOURTH_INDICATOR_MID_POINT, INDICATOR-INDICATOR_THICKNESS, 0)

    def turn_off_indicator(self):
        pygame.draw.circle(self.screen, BLACK,   FIRST_INDICATOR_MID_POINT, INDICATOR, 0)
        pygame.draw.circle(self.screen, WHITE,   FIRST_INDICATOR_MID_POINT, INDICATOR, INDICATOR_THICKNESS)
        pygame.draw.circle(self.screen, BLACK,   SECOND_INDICATOR_MID_POINT, INDICATOR, 0)
        pygame.draw.circle(self.screen, WHITE,   SECOND_INDICATOR_MID_POINT, INDICATOR, INDICATOR_THICKNESS)
        pygame.draw.circle(self.screen, BLACK,   THIRD_INDICATOR_MID_POINT, INDICATOR, 0)
        pygame.draw.circle(self.screen, WHITE,   THIRD_INDICATOR_MID_POINT, INDICATOR, INDICATOR_THICKNESS)
        pygame.draw.circle(self.screen, BLACK,   FOURTH_INDICATOR_MID_POINT, INDICATOR, 0)
        pygame.draw.circle(self.screen, WHITE,   FOURTH_INDICATOR_MID_POINT, INDICATOR, INDICATOR_THICKNESS)


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
        self.offsetX             = 19                     # offset for needle, x-position
        self.offsetY             = 19                     # offset for needle, y-position
        self.indicator           = Indicator(self.screen) # create an Indicator instance
        self.scale               = scale                  # set scale of needle, default = IMAGE_SCALE

    def reset_parameters(self):
        """
        Reset needle.
        """
        self.angle         = 0
        self.rpm           = 0  
        self.mousePressed  = False
        self.indicator.turn_off_indicator()

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
                    self.angle += 2
                self.angle += self.speed

            # rotate leftInstrument clock wise
            elif int(self.angle) > rotation:
                if (abs(self.angle-rotation) > TEST_ROT_SPEED):
                    self.angle -= 2
                self.angle -= self.speed

            else:
                print 'Stopped'

            # clear flag when instrument has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False
                self.indicator.turn_on_indicator(self.instrumentIndex)

        # rotate needle
        self.image = pygame.transform.rotozoom(self.needleImage, self.angle, self.scale)

        # reset the center
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)

    def blit_needle(self):
        self.screen.blit(self.image, self.rect)

    def instrument_update(self, degAngle):
        """
        """
        self.rotate(degAngle)

        self.rect.center += np.asarray(self.instrumentMidPoint)
        self.rect.center += np.array([np.cos(math.radians(self.angle)) * self.offsetX,
                                      -np.sin(math.radians(self.angle)) * self.offsetY])

        self.blit_needle()


