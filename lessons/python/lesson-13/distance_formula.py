import math

def double(n):
    return n ** 2

def distance(x1, y1, x2, y2):
    return math.sqrt(double(x1 - x2) + double(y1 - y2))

print(distance(1, 1, 4, 3))
