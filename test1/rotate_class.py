import math
import pygame
import sys
from pygame.locals import *

# define colors
RED  = (255,0,0)
BLUE = (0,0,255)

pygame.init()
screen = pygame.display.set_mode((800,800),0,32)

class Arrow:
    def __init__(self):
        # size of vector
        self.dx = 100 
        self.dy = 0

    def rotate_vector(self, angle):
        xNorm  = self.dx * math.cos(math.radians(angle)) - self.dy * math.sin(math.radians(angle))
        yNorm  = self.dx * math.sin(math.radians(angle)) + self.dy * math.cos(math.radians(angle))
        radius = math.sqrt(self.dx*self.dx + self.dy*self.dy)
        return xNorm, yNorm, radius

    def move_vector(self, xOrig, yOrig, a, b):
        x = xOrig + a
        y = yOrig - b
        return x, y
    

arrow = Arrow()

# rotate angel
angle = 0

# running flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            xOrigo = pos[0]
            yOrigo = pos[1]

            while angle < 360:
                # calculate new coordinates
                xNorm, yNorm, radius = arrow.rotate_vector(angle)
            
                # move to new origo position
                x, y = arrow.move_vector(xOrigo, yOrigo, xNorm, yNorm)
            
                pygame.draw.line(screen, RED,  (xOrigo,yOrigo), (x,y), 2)
            
                angle += 60

    pygame.display.update()
    angle = 0

print 40*'-'
print 'Radius:',radius
pygame.quit()
