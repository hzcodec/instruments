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

        self.speed        = 0.04  # rotation speed of needle => 1.47 degrees
        self.reduceSpeed  = 0.0   # reduce speed value
        self.angle        = 0.0   # current angle in radians
        self.startAngle   = 0.0   # start angle in radians
        self.stopAngle    = 0.0   # stop angle for needle in radians
        self.rpm          = 0     # number of rpm

        self.mousePressed = False  # flag indicating when mouse is pressed

    def reset_parameters(self):
        self.reduceSpeed   = 0.0
        self.angle         = 0.0
        self.startAngle    = 0.0
        self.stopAngle     = 0.0
        self.rpm           = 0  
        self.mousePressed  = False

    def set_flag(self, flag):
        """
        Set flag to indicate whether the mouse was pressed or not.
        """
        self.mousePressed = flag

    def rotate(self, rotation):
        """
        Rotates and re-centers the needle.
        """

        # if mouse button pressed then check if stop angle is reached
        if self.mousePressed:
          self.rpm += 1

          # move needle
          self.angle = rotation

        self.mousePressed = False

        # rotate our image 
        image = pygame.transform.rotozoom(self.base, np.degrees(self.angle), IMAGE_SCALE)

        # reset the center
        rect = image.get_rect()
        rect.center = (0, 0)
 
        return image, rect


# position window 
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d, %d" % WINDOW_POS

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()
 
needle = Needle('../pic/needle3.gif')
needle.set_flag(True)

displayMidPoint = (WIDTH/2, HEIGHT/2)

# rotation point of needle image
offset1 = 99
offset2 = 99

# set needle at zero position
radianAngle = math.radians(220.0)

currentPos   = (0, 0)
stopAngle    = 0

#fname = "instr.png"
background = pygame.image.load("pictures/instr2.png")
bgRect = background.get_rect()
 
while 1:
 
    display.fill(WHITE)
 
    needleImage, needleRect = needle.rotate(radianAngle) 
    needleRect.center += np.asarray(displayMidPoint)
    needleRect.center += np.array([np.cos(needle.angle) * offset1,
                                  -np.sin(needle.angle) * offset2])
 
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
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(220)

            elif event.key == pygame.K_1:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(200)

            elif event.key == pygame.K_2:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(180)

            elif event.key == pygame.K_3:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(160)

            elif event.key == pygame.K_4:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(140)

            elif event.key == pygame.K_5:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(120)

            elif event.key == pygame.K_6:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(100)

            elif event.key == pygame.K_7:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(80)

            elif event.key == pygame.K_8:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(60)

            elif event.key == pygame.K_9:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(40)

            elif event.key == pygame.K_PLUS:
                needle.reset_parameters()
                needle.set_flag(True)
                radianAngle = math.radians(20)
            
    lblAngleDeg = myfont.render("Current angle: "+str(math.degrees(radianAngle))+" deg", 0, BLACK)
    display.blit(lblAngleDeg, (280,450))

    pygame.display.update()
    fpsClock.tick(30)

