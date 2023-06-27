import math

def circcoll(x1, y1, r1, x2, y2, r2):
    Y = y2 - y1
    X = x2 - x1
    d = math.sqrt(X*X + Y*Y)
    if(r1+r2 > d): return True
    return False
