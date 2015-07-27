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
LEFT  = 1
RIGHT = 3

# start angle for needle
START_AT_ANGLE = 0.0


def get_parameters_via_mouse(mousePosition):
    """
    Set stop angle and the reduce speed variable.
    Use the mouse position (x-axis) to select stop angle.
    """

    stop_at_angle = mousePosition[0]
    return stop_at_angle


class Needle:
    """
    A class for storing relevant arm segment information.
    """
    def __init__(self, image):
        self.base = pygame.image.load(image)

        self.speed         = 0.02  # rotation speed of needle => 1.47 degrees
        self.reduceSpeed   = 0.0   # reduce speed value
        self.angle         = 0.0   # current angle in radians
        self.startAngle    = 0.0   # start angle in radians
        self.stopAngle     = 0.0   # stop angle for needle in radians

        self.rpm = 0 # number of rpm

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
 
    def set_initial_angles(self, start, stop):
        """
        Set start and stop angles for needle in degrees. The angles are converted to radians.
        """
        self.stopStart = math.radians(start)
        self.stopAngle = math.radians(stop)

    def rotate(self, rotation):
        """
        Rotates and re-centers the needle.
        """

        deltaAngle = self.stopAngle - self.startAngle

        # if mouse button pressed then check if stop angle is reached
        if self.mousePressed:
          self.rpm   += 1

          if self.angle < self.stopAngle:

              # move needle
              self.angle += self.speed - self.reduceSpeed

              # if less than 45 degrees then start to slow down needle
              lessThan45Degrees = self.stopAngle - self.angle
              if lessThan45Degrees < 0.79:
                  self.reduceSpeed += 0.00025

          else:
              print '*** Stopped at:',round(math.degrees(self.angle),1)
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
 
needle = Needle('../pic/needle2.gif')
displayMidPoint = (WIDTH/2, HEIGHT/2)

# rotation point of needle image
offset1 = 99
offset2 = 99
radianAngle = math.radians(0)

currentPos   = (0, 0)
stopAngle    = 0
 
while 1:
 
    display.fill(WHITE)
 
    needleImage, needleRect = needle.rotate(radianAngle) 
    needleRect.center += np.asarray(displayMidPoint)
    needleRect.center += np.array([np.cos(needle.angle) * offset1,
                                  -np.sin(needle.angle) * offset2])
 
    display.blit(needleImage, needleRect)
    pygame.draw.line(display, RED, (250,10), (250,490), 2)
    pygame.draw.line(display, RED, (10,250), (490,250), 2)

    myfont = pygame.font.SysFont("monospace", 15) 
    
 
    # check for events, [quit, mouse click]
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()

        # start moving the needle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            needle.set_flag(True)
            needle.set_initial_angles(0.0, stopAngle)

        # reset the needle
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            print 'Restart'
            needle.reset_parameters()

        # set angle by using the mouse position (x-axis)
        elif event.type == pygame.MOUSEMOTION:
            currentPos = event.pos
            stopAngle = get_parameters_via_mouse(currentPos)
            
    lblAngleDeg = myfont.render("Stop angle: "+str(stopAngle)+" deg", 0, BLACK)
    lblAngleRad = myfont.render("Stop angle: "+str(round(math.radians(stopAngle),2))+" rad", 0, BLACK)
    display.blit(lblAngleDeg, (50,20))
    display.blit(lblAngleRad, (50,40))

    pygame.display.update()
    fpsClock.tick(30)

