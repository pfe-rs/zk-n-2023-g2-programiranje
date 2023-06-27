import math

def kolizija(rectx, recty, width, height,   
              center_x, center_y, radius):  
    testX = center_x
    testY = center_y

    if(center_x < rectx):
        testX = rectx
    else:
        if(center_x > rectx + width):
            testX = rectx + width

    if(center_y < recty):
        testY = recty
    else:
        if(center_y > recty + height):
            testY = recty + height

    distanceX = center_x - testX
    distanceY = center_y - testY

    distance = math.sqrt(distanceX*distanceX + distanceY*distanceY)

    if(distance < radius):
        return True
    else:
        return False