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
        pygame.draw.circle(self.screen, BLACK,   (xPos,yPos), 15, 0)
        pygame.draw.circle(self.screen, WHITE,   (xPos,yPos), 15, 2)

    def turn_on_indicator(self, instNr):
        if instNr == 1:
            pygame.draw.circle(self.screen, RED,   (xPos,yPos), 15, 0)
        elif instNr == 2:
            pygame.draw.circle(self.screen, BLUE,   (xPos+265,yPos), 15, 0)
        elif instNr == 3:
            pygame.draw.circle(self.screen, GREEN,   (xPos+505,yPos), 15, 0)
        elif instNr == 4:
            pygame.draw.circle(self.screen, YELLOW,   (xPos+765,yPos), 15, 0)

    def turn_off_indicator(self):
        pygame.draw.circle(self.screen, BLACK,   (xPos,yPos), 15, 0)
        pygame.draw.circle(self.screen, BLACK,   (xPos+265,yPos), 15, 0)
        pygame.draw.circle(self.screen, BLACK,   (xPos+505,yPos), 15, 0)
        pygame.draw.circle(self.screen, BLACK,   (xPos+765,yPos), 15, 0)

        pygame.draw.circle(self.screen, WHITE,   (xPos,yPos), 15, 2)
        pygame.draw.circle(self.screen, WHITE,   (xPos+265,yPos), 15, 2)
        pygame.draw.circle(self.screen, WHITE,   (xPos+505,yPos), 15, 2)
        pygame.draw.circle(self.screen, WHITE,   (xPos+765,yPos), 15, 2)


class Instrument:
    """
    A class for handling the instrument.
    """
    def __init__(self, screen, image, middlePoint):
        """
        input parameters:
          screen              -  Current surface name
          image               -  Image of needle
          middlePoint         -  Middle point of instrument
        """
        self.needleImage      = pygame.image.load(image)
        self.speed            = 2
        self.angle            = 0
        self.rpm              = 0      # number of rpm, used for test purpose
        self.mousePressed     = False  # flag indicating when mouse is pressed
        self.instrumentMidPoint  = middlePoint
        self.screen  = screen

        #self.speed            = rotationSpeed
        #self.angle            = angle
        #self.instrumentNumber = instrumentNumber

#        self.indicator    = Indicator(self.screen) # create an Indicator instance

    def reset_parameters(self):
        """
        Reset needle.
        """
        self.angle         = 0
        self.rpm           = 0  
        self.mousePressed  = False
        #self.indicator.turn_off_indicator()

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

            # rotate leftInstrument counter clock wise
            if int(self.angle) < rotation:
                self.angle += self.speed

            # rotate leftInstrument clock wise
            elif int(self.angle) > rotation:
                self.angle -= self.speed

            else:
                print 'Stopped'
                #self.indicator.turn_off_indicator()

            # clear flag when leftInstrument has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False
                #self.indicator.turn_on_indicator(self.instrumentNumber)

        # rotate needle
        self.image = pygame.transform.rotozoom(self.needleImage, self.angle, IMAGE_SCALE)

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
        self.rect.center += np.array([np.cos(math.radians(self.angle)) * 19,
                                      -np.sin(math.radians(self.angle)) * 19])

        self.blit_needle()


