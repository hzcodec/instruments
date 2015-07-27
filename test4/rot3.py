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


origin_x = 300
origin_y = 300
rotation = 45
image_width = 100
image_height = 10
image_width_n = 100
image_height_n = 10

x,y = get_rotation_offset(origin_x, origin_y, rotation, image_width, image_height, image_width_n,  image_height_n)

print x
print y
