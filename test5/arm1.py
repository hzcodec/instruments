import numpy as np
import pygame
import pygame.locals
import sys
import os

IMAGE_SCALE = 1
CIRCLE_SIZE = 5
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
WHITE = (255, 255, 255)
WIDTH  = 500
HEIGHT = 500

class ArmPart:
    """
    A class for storing relevant arm segment information.
    """
    def __init__(self, pic, scale=1.0):
        self.base = pygame.image.load(pic)
        # some handy constants
        self.length = self.base.get_rect()[2]
        self.scale = self.length * scale
        self.offset = self.scale / 2.0
 
        self.rotation = 0.0 # in radians
        print 50*'-'
        print 'length:',self.length,' offset:',self.offset
        print 'Image size:',self.base.get_rect()
        print 50*'-'
 
    def rotate(self, rotation):
        """
        Rotates and re-centers the arm segment.
        """
        self.rotation += rotation 
        # rotate our image 
        image = pygame.transform.rotozoom(self.base, np.degrees(self.rotation), IMAGE_SCALE)
        # reset the center
        rect = image.get_rect()
        rect.center = (0, 0)
 
        return image, rect

 
os.environ["SDL_VIDEO_CENTERED"] = '1'

pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
fpsClock = pygame.time.Clock()
 
upperarm = ArmPart('../pic/needle2.gif', scale=1.0)
midPoint = (WIDTH/2, HEIGHT/2)

# 116.5 => end of arrow, 0 => mid of arrow, -116.5 => tip of arrow
offset1 = 99
offset2 = 99
 
while 1:
 
    display.fill(WHITE)
 
    ua_image, ua_rect = upperarm.rotate(.03) 
    ua_rect.center += np.asarray(midPoint)
#    ua_rect.center -= np.array([np.cos(upperarm.rotation) * upperarm.offset,
#                                -np.sin(upperarm.rotation) * upperarm.offset])
    ua_rect.center += np.array([np.cos(upperarm.rotation) * offset1,
                                -np.sin(upperarm.rotation) * offset2])
#    print 'rotation:',upperarm.rotation,'  center:',ua_rect.center,'  offset:',upperarm.offset
 
    display.blit(ua_image, ua_rect)
    pygame.draw.circle(display, BLUE, midPoint, CIRCLE_SIZE)
    pygame.draw.line(display, (0,255,0), (250,250), (366,250), 6)
    pygame.draw.line(display, (255,0,0), (250,10), (250,490), 2)
    pygame.draw.line(display, (255,0,0), (10,250), (490,250), 2)
 
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    fpsClock.tick(30)

