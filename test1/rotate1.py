import math

import pygame
import sys
from pygame.locals import *

RED  = (255,0,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((600,600),0,32)

angle   = 40
length  = 300

xOrigin = 100
yOrigin = 400

x = 1
y = 0

x2 = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
y2 = x * math.sin(math.radians(angle)) - y * math.cos(math.radians(angle))

print 'x2:',x2
print 'y2:',y2
x22 = xOrigin+x2*length
y22 = yOrigin-y2*length
print x22,y22

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen, RED,  (xOrigin,yOrigin), (xOrigin+300,yOrigin), 2)
    pygame.draw.line(screen, BLUE, (xOrigin,yOrigin), (x22,y22), 2)

    pygame.display.update()
