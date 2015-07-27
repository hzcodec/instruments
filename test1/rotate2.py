import math

import pygame
import sys
from pygame.locals import *

RED  = (255,0,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((800,800),0,32)

xOrigin = 0
yOrigin = 400

xOrigo = 0
yOrigo = 400

xStart = 0
yStart = 400

angle = 30
dx = 300 
dy = 0

xNorm = dx * math.cos(math.radians(angle)) - dy * math.sin(math.radians(angle))
yNorm = dx * math.sin(math.radians(angle)) + dy * math.cos(math.radians(angle))
r     = math.sqrt(dx*dx + dy*dy)

print 40*'-'
print 'xNorm:',xNorm
print 'yNorm:',yNorm
print 'r:    ',r

# move to new origo
x = xOrigo + xNorm
y = yOrigo - yNorm

print 'x:',x
print 'y:',y
print 40*'-'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen, BLUE, (xStart,yStart), (xOrigo+r,yOrigin), 2)
    pygame.draw.line(screen, RED,  (xOrigo,yOrigo), (x,y), 2)

    pygame.display.update()
