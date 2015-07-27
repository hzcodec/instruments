import numpy as np
import pygame
import pygame.locals
import sys
import math
import os

IMAGE_SCALE    = 1

# define colors
BLACK          = (0, 0, 0)
RED            = (255, 0, 0)
BLUE           = (0, 0, 255)
WHITE          = (255, 255, 255)

# window size and position
WIDTH          = 500
HEIGHT         = 500
WINDOW_POS     = (30,30)

# start angle for needle
START_AT_ANGLE = 0.0


def get_parameters_via_mouse(mousePosition):
    """
    Set stop angle and the reduce speed variable.
    Use the mouse position (x-axis) to select stop angle.
    """

    stop_at_angle = 22.5
    reducedSpeed = 0.000522

    if mousePosition[0] > 100:
        stop_at_angle  = 45 
        reducedSpeed = 0.00025
    if mousePosition[0] > 150:
        stop_at_angle  = 90 
        reducedSpeed = 0.000125 
    if mousePosition[0] > 200:
        stop_at_angle  = 135 
        reducedSpeed = 0.000085 
    if mousePosition[0] > 250:
        stop_at_angle  = 180 
        reducedSpeed = 0.000063 
    if mousePosition[0] > 300:
        stop_at_angle  = 270 
        reducedSpeed = 0.000042  
    if mousePosition[0] > 350:
        stop_at_angle  = 315 
        reducedSpeed = 0.000036 
    if mousePosition[0] > 400:
        stop_at_angle  = 360 
        reducedSpeed = 0.0000315

    return stop_at_angle, reducedSpeed


class Needle:
    """
    A class for storing relevant arm segment information.
    """
    def __init__(self, pic, scale=1.0):
        self.base = pygame.image.load(pic)

        self.length = self.base.get_rect()[2]
        self.scale = self.length * scale
        self.offset = self.scale / 2.0

        self.speed         = 0.02  # rotation speed of needle => 1.47 degrees
        self.reduceSpeed   = 0.0   # reduce speed value
        self.angle         = 0.0   # current angle in radians
        self.startAngle    = 0.0   # start angle in radians
        self.stopAngle     = 0.0   # stop angle for needle in radians
        self.rSpeed        = 0.0   # reduced speed, constant

        self.rpm = 0 # number of rpm

        self.mousePressed = False  # flag indicating when mouse is pressed

    def set_flag(self, flag):
        """
        Set flag to indicate whether the mouse was pressed or not.
        """
        self.mousePressed = flag
 
    def set_initial_angles(self, start, stop, speed):
        """
        Set start and stop angles for needle in degrees. The angles are converted to radians.
        """
        self.stopStart = math.radians(start)
        self.stopAngle = math.radians(stop)
        self.rSpeed = speed

    def rotate(self, rotation):
        """
        Rotates and re-centers the needle.
        """

        deltaAngle = self.stopAngle - self.startAngle
        #print 'rpm:',self.rpm,' - angle',self.angle,' - deltaAngle:',deltaAngle,' - reduceSpeed',self.reduceSpeed

        # if mouse button pressed then check if stop angle is reached
        if self.mousePressed:
          self.rpm   += 1

          if self.angle < self.stopAngle:

              # if not reached then slow down arrow speed depending on distance to stop angle
              self.angle += self.speed - self.reduceSpeed
              self.reduceSpeed += self.rSpeed

          else:
              print '*** Stopped at:',self.angle
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
 
needle = Needle('../pic/needle2.gif', scale=1.0)
displayMidPoint = (WIDTH/2, HEIGHT/2)

# rotation point of needle image
offset1 = 99
offset2 = 99
radianAngle = math.radians(0)

currentPos   = (0, 0)
reducedSpeed = 0.0
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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            needle.set_flag(True)
            needle.set_initial_angles(0.0, stopAngle, reducedSpeed)

        elif event.type == pygame.MOUSEMOTION:
            currentPos = event.pos
            stopAngle, reducedSpeed = get_parameters_via_mouse(currentPos)
            
    label2 = myfont.render("Stop angle: "+str(stopAngle), 0, BLACK)
    display.blit(label2, (100,20))

    pygame.display.update()
    fpsClock.tick(30)

