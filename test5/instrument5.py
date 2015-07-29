import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

IMAGE_SCALE = 1

# define colors
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
BLUE   = (0, 0, 255)
GREEN  = (0, 255, 0)
WHITE  = (255, 255, 255)

# window size and position
WIDTH      = 500
HEIGHT     = 500
WINDOW_POS = (30,30)

# define mouse buttons
RIGHT = 3

# define instrument's middle point
INSTRUMENT_MIDDLE_POINT = (250, 250)


class Instrument:
    """
    Instrument class.
      Input:
        image       - Image of needle.
        middlePoint - Middle point of instrument
    """
    def __init__(self, image, middlePoint):
        self.needleImage        = pygame.image.load(image)  
        self.speed              = 2             # rotation speed of needle
        self.angle              = 0             # current angle in degrees
        self.rpm                = 0             # number of rpm, used for test purpose
        self.mousePressed       = False         # flag indicating when mouse is pressed
        self.instrumentMidPoint = middlePoint   # mid point of needle

        # rotation point of needle image
        self.offset1 = 99
        self.offset2 = 99

    def reset_parameters(self):
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
            image = pygame.transform.rotozoom(self.needleImage, self.angle, IMAGE_SCALE)
            rect = image.get_rect()
            rect.center = (0, 0)
            return image, rect

    def rotate(self, rotation):
        """
        Rotates and re-centers the needle.
        """

        # if mouse button pressed then rotate needle
        if self.mousePressed:

            # increment loop counter, used for debug purpose
            self.rpm += 1

            # rotate needle counter clock wise
            if int(self.angle) < rotation:
                self.angle += self.speed

            # rotate needle clock wise
            elif int(self.angle) > rotation:
                self.angle -= self.speed

            else:
                print 'Stopped'

            # clear flag when needle has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False

        # rotate needle
        self.image = pygame.transform.rotozoom(self.needleImage, self.angle, IMAGE_SCALE)

        # reset the center
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
 
    def blit_needle(self):
        screen.blit(self.image, self.rect)

    def instrument_update(self, degAngle):
        self.rotate(degAngle) 

        self.rect.center += np.asarray(self.instrumentMidPoint)
        self.rect.center += np.array([np.cos(math.radians(self.angle)) * self.offset1,
                                     -np.sin(math.radians(self.angle)) * self.offset2])

        self.blit_needle()


# position window at WINDOW_POS
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

# initialize pygame and set window size
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

fpsClock = pygame.time.Clock()
 
# initialize instrument instance
instrument = Instrument('../pic/red_needle.png', INSTRUMENT_MIDDLE_POINT)

# set instrument angle at start position in degrees
degAngle = -20.0
instrument.set_needle_position(degAngle)

# load background image
background = pygame.image.load("../pic/background3.png")
bgRect     = background.get_rect()

inputData = 0.0


while 1:
 
    screen.fill(BLACK)
 
    screen.blit(background, bgRect)
    instrument.instrument_update(degAngle)

    # check for events, [quit, mouse click]
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        # reset the instrument
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print 'Restart'
            instrument.reset_parameters()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                instrument.set_flag(True)
                inputData = 1.0 

            elif event.key == pygame.K_2:
                instrument.set_flag(True)
                inputData = 6.5 

            elif event.key == pygame.K_3:
                instrument.set_flag(True)
                inputData = 12.0

            elif event.key == pygame.K_4:
                instrument.set_flag(True)
                inputData = 2.8

            y = -20*inputData + 220
            degAngle = y
            print 'degAngle:',degAngle

    pygame.display.update()
    fpsClock.tick(30)

