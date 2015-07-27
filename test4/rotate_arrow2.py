import pygame
import pygame.locals
import math
 
def get_rotation_offset(origin_x, origin_y, rotation, image_width,
                        image_height, image_width_normal,
                        image_height_normal):

    # Return what to offset an origin when the object is rotated as a
    # two-part tuple: (x_offset, y_offset)
    x_offset = 0
    y_offset = 0

    if rotation % 180:
        # Adjust offset for the borders getting bigger.
        x_offset += (image_width - image_width_normal) / 2
        y_offset += (image_height - image_height_normal) / 2

    if rotation % 360:
        # Rotate about the origin
        center_x = image_width_normal / 2
        center_y = image_height_normal / 2
        xorig = origin_x - center_x
        yorig = origin_y - center_y
        start_angle = math.atan2(-yorig, xorig)
        new_angle = start_angle + math.radians(rotation)
        radius = math.hypot(xorig, yorig)
        new_center_x = origin_x + radius * math.cos(new_angle)
        new_center_y = origin_y - radius * math.sin(new_angle)
        x_offset += new_center_x + center_x
        y_offset += new_center_y + center_y

    return (x_offset, y_offset)


WHITE = (255, 255, 255)
 
pygame.init()
 
display  = pygame.display.set_mode((600, 600))
fpsClock = pygame.time.Clock()
 
# pixel size: 35, 233
image = pygame.image.load('../pic/needle2.gif')
print 'Image size:',image.get_rect()

xPos             = 300    # x position for arrow
yPos             = 300    # y position for arrow
angle            = 45     # start angle
idx              = 0      # index
spinn            = 0      # spinning counter
reducedSpeed     = 0      # new reduced speed => new angle
noOfSpinningLaps = 145    # number of laps before arrow starts to slow down
rotateSpeed      = 6      # initial rotation speed (angle)
scaleFactor      = 0.02   # reduce factor, how fast arrow is slowed down
stoppSpeed       = 0.02   # final stopp

while 1:
 
    display.fill(WHITE)
    rotated_image = pygame.transform.rotate(image, angle)

    rect = rotated_image.get_rect()
    print 'rect:',rect
    rect.center = (300,300)

#    x,y = get_rotation_offset(origin_x, origin_y, 45, image_width,
#                              image_height, image_width_normal,
#                              image_height_normal):

    display.blit(rotated_image, rect)

    pygame.draw.line(display, (255,0,0), (300,10), (300,590), 2)
    pygame.draw.line(display, (255,0,0), (10,300), (590,300), 2)
    pygame.draw.rect(display, (0,0,255), (0,0,189,189), 2)

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    fpsClock.tick(30)


#myimage.center = rotPoint(myimage.center, (300,300), 45)


#http://www.gamedev.net/topic/557694-pythonpygame-rotation-around-a-point-complications/

