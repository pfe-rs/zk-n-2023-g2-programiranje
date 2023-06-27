import math
'''detecting collision between two circles'''

def collision(rleft, rtop, width, height,   
              center_x, center_y, radius): 
    
    x_center = rleft + width / 2
    y_center = rtop + height / 2
    r_radius = width / 2
    distance = math.sqrt((x_center - center_x) ** 2 + (y_center -center_y) ** 2)

    if distance <= (r_radius + radius):
        return True
    return False 
