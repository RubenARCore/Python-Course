import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def closest_point(x1, y1, x2, y2):
    d1 = x1 * x1 + y1 * y1
    d2 = x2 * x2 + y2 * y2

    if d1 <= d2:
        x, y = x1, y1
    else:
        x, y = x2, y2

    return math.floor(x), math.floor(y)

x, y = closest_point(x1, y1, x2, y2)

print(f'({x}, {y})')