import math


def rotatePoint(origin, angle):
        x = 100
        y = 10
        radius = math.hypot(x,y)
        print 'radius:',radius

        sinT = math.sin(math.radians(angle))
        cosT = math.cos(math.radians(angle))
        
        print origin[0] + (cosT * (x - origin[0]) - sinT * (y - origin[1]))
        print origin[1] + (sinT * (x - origin[0]) + cosT * (y - origin[1]))



origin = (300,300)
angle  = 45

rotatePoint(origin, angle)

