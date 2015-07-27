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


class Needle:
    """
    A class for storing relevant arm segment information.
    """
    def __init__(self, image):
        self.base = pygame.image.load(image)

        self.speed        = 2      # rotation speed of needle
        self.angle        = 0      # current angle in radians
        self.rpm          = 0      # number of rpm, used for test purpose
        self.mousePressed = False  # flag indicating when mouse is pressed

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
            image = pygame.transform.rotozoom(self.base, self.angle, IMAGE_SCALE)
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
        image = pygame.transform.rotozoom(self.base, self.angle, IMAGE_SCALE)

        # reset the center
        rect = image.get_rect()
        rect.center = (0, 0)
 
        return image, rect

    def blit_images(self, background, bgRect, greenLight, greenLightRect, needleImage, needleRect, keyFlag):
        display.blit(background, bgRect)

        if keyFlag == 1 and not self.mousePressed:
            #display.blit(greenLight, greenLightRect)
            display.blit(lblError, (45,420))
        if keyFlag == 2 and not self.mousePressed:
            display.blit(redLight, redLightRect)
            display.blit(lblOK, (45,420))

        display.blit(needleImage, needleRect)


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()
display  = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()
 
needle = Needle('../pic/red_needle.png')
needle.set_flag(True)

displayMidPoint = (WIDTH/2, HEIGHT/2)

# rotation point of needle image
offset1 = 99
offset2 = 99

# set needle at start position
degAngle = -20.0
needle.set_needle_position(degAngle)

# load images
background     = pygame.image.load("../pic/background3.png")
greenLight     = pygame.image.load("../pic/green.png")
redLight       = pygame.image.load("../pic/red.png")
bgRect         = background.get_rect()
greenLightRect = greenLight.get_rect()
redLightRect   = redLight.get_rect()

inputData = 0.0
keyFlag = 0

# define headline, font type and text messages
pygame.display.set_caption("                                  *** POSITION ***")
messageFont = pygame.font.SysFont("None", 28) 
lblError    = messageFont.render("ERROR", 0, RED)
lblOK       = messageFont.render("OK", 0, GREEN)


while 1:
 
    display.fill(BLACK)
 
    needleImage, needleRect = needle.rotate(degAngle) 
    needleRect.center += np.asarray(displayMidPoint)
    needleRect.center += np.array([np.cos(math.radians(needle.angle)) * offset1,
                                  -np.sin(math.radians(needle.angle)) * offset2])
 
    needle.blit_images(background, bgRect, greenLight, greenLightRect, needleImage, needleRect, keyFlag)
 
    # check for events, [quit, mouse click]
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        # reset the needle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print 'Restart'
            needle.reset_parameters()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                needle.set_flag(True)
                inputData = 1.0 
                keyFlag = 1

            elif event.key == pygame.K_2:
                needle.set_flag(True)
                inputData = 6.5 
                keyFlag = 2

            elif event.key == pygame.K_3:
                needle.set_flag(True)
                inputData = 12.0
                keyFlag = 3

            elif event.key == pygame.K_4:
                needle.set_flag(True)
                inputData = 2.8
                keyFlag = 4

            y = -20*inputData + 220
            degAngle = y

    lblInputData = messageFont.render("Input data: "+str(inputData), 0, WHITE)
    display.blit(lblInputData, (195,380))

    pygame.display.update()
    fpsClock.tick(30)

