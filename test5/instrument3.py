import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

IMAGE_SCALE = 1

# define colors
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)

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

        self.speed        = 1      # rotation speed of needle
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
                pass

            # clear flag when needle has reached final position
            if (int(self.angle) == rotation):
                self.mousePressed = False

        # rotate needle
        image = pygame.transform.rotozoom(self.base, self.angle, IMAGE_SCALE)

        # reset the center
        rect = image.get_rect()
        rect.center = (0, 0)
 
        return image, rect


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()
display  = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()
 
needle = Needle('../pic/needle3.gif')
needle.set_flag(True)

displayMidPoint = (WIDTH/2, HEIGHT/2)

# rotation point of needle image
offset1 = 99
offset2 = 99

# set needle at zero position
degAngle = 220.0
needle.set_needle_position(degAngle)

background = pygame.image.load("pictures/instr2.png")
bgRect = background.get_rect()
 
while 1:
 
    display.fill(WHITE)
 
    needleImage, needleRect = needle.rotate(degAngle) 
    needleRect.center += np.asarray(displayMidPoint)
    needleRect.center += np.array([np.cos(math.radians(needle.angle)) * offset1,
                                  -np.sin(math.radians(needle.angle)) * offset2])
 
    display.blit(background, bgRect)
    display.blit(needleImage, needleRect)

    myfont = pygame.font.SysFont("monospace", 15) 
 
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
            if event.key == pygame.K_0:
                needle.set_flag(True)
                degAngle = 220

            elif event.key == pygame.K_1:
                needle.set_flag(True)
                degAngle = 200

            elif event.key == pygame.K_2:
                needle.set_flag(True)
                degAngle = 180

            elif event.key == pygame.K_3:
                needle.set_flag(True)
                degAngle = 160

            elif event.key == pygame.K_4:
                needle.set_flag(True)
                degAngle = 140

            elif event.key == pygame.K_5:
                needle.set_flag(True)
                degAngle = 120

            elif event.key == pygame.K_6:
                needle.set_flag(True)
                degAngle = 100

            elif event.key == pygame.K_7:
                needle.set_flag(True)
                degAngle = 80

            elif event.key == pygame.K_8:
                needle.set_flag(True)
                degAngle = 60

            elif event.key == pygame.K_9:
                needle.set_flag(True)
                degAngle = 40

            elif event.key == pygame.K_PLUS:
                needle.set_flag(True)
                degAngle = 20
            
    lblAngleDeg = myfont.render("Current angle: "+str(degAngle)+" deg", 0, BLACK)
    display.blit(lblAngleDeg, (280,450))

    pygame.display.update()
    fpsClock.tick(30)

