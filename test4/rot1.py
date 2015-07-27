import math

def rotPoint(point, axis, ang):

    x = point[0] - axis[0]
    y = point[1] - axis[1]
    print 'x:',x
    print 'y:',y

    radius = math.sqrt(x*x + y*y) # get the distance between points
    print 'radius:',radius
    
    RAng = math.radians(ang)       # convert ang to radians.
    print 'Rang:',RAng
    
    h = axis[0] + (radius * math.cos(RAng))
    v = axis[1] + (radius * math.sin(RAng))
    
    return h, v


p = [35,233]
a = [300,300]
angle = 45

h,v = rotPoint(p, a, angle)

print 'h',h
print 'v',v

#myimage.center = rotPoint(myimage.center, (300,300), 45)
