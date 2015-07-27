import pygame
import pygame.locals
import math
 
WHITE = (255, 255, 255)
 
pygame.init()
 
display  = pygame.display.set_mode((600, 600))
fpsClock = pygame.time.Clock()
 
image = pygame.image.load('blue_arrow.png')
print 'Image size:',image.get_rect()

angle = 0.
speed = 4 
laps  = 0
flag1  = True
flag2  = True
flag3  = True
flag4  = True
 
xPos = 300
yPos = 300

while 1:
 
    display.fill(WHITE)
    #rotated_image = pygame.transform.rotozoom(image, angle, 0.5)

    #rect = rotated_image.get_rect()
    #surface_center = rotated_image.get_rect().center
    mx = 100
    my = 100
    ang = math.atan2((my-300),-(mx-300))
    rPic = pygame.transform.rotate(image, math.degrees(ang))
    x = 300 -rPic.get_width()/2
    y = 300 -rPic.get_height()/2
    

    #rect.center = (300,300)
    #display.blit(rotated_image, rect)
    display.blit(rPic,(x,y))

    pygame.draw.line(display, (255,0,0), (300,10), (300,590), 2)
    pygame.draw.line(display, (255,0,0), (10,300), (590,300), 2)
 
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
 
    if angle > 359:
        flag4 = True
        angle = 0
        if flag1:
            laps  += 1
            flag1 = False
            speed = 0.5

    elif angle > 270:
        flag1 = True
        if flag2:
            laps  += 1
            flag2 = False
            speed = 1

    elif angle > 180:
        flag2 = True
        if flag3:
            laps  += 1
            flag3 = False
            speed = 2

    elif angle > 90:
        flag3 = True
        if flag4:
            laps  += 1
            flag4 = False
            speed = 3

    angle += speed

    #print 'Speed:',speed
    #print 'Angle:',angle
    #print 'Laps: ',laps

    fpsClock.tick(30)


# I think something like this should do what you are looking for.
# 
# from math import *
# 
# def rotPoint(point, axis, ang):
#      """ Orbit. calcs the new loc for a point that rotates a given num 
# of degrees around an axis point,
#          +clockwise, -anticlockwise -> tuple x,y
#      """
#      x, y = point[0] - axis[0], point[1] - axis[1]
#      radius = sqrt(x*x + y*y) # get the distance between points
# 
#      RAng = radians(ang)       # convert ang to radians.
# 
#      h = axis[0] + ( radius * cos(RAng) )
#      v = axis[1] + ( radius * sin(RAng) )
# 
#      return h, v
# 
# 
# myimage.center = rotPoint(myimage.center, (300,300), 45)
# 
# this line should rotate myimage.center around point (300,300) by 45 degrees

# rotationCenter = (myimage.center[0]+10,myimage.center[1]+20)
# myimage = rotateImage(myimage,rotationCenter, 45) 
