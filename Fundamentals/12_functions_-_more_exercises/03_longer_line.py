import math

def distance_from_origin(x, y):
    return x * x + y * y

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def closer_point(x1, y1, x2, y2):
    if distance_from_origin(x1, y1) <= distance_from_origin(x2, y2):
        return (x1, y1, x2, y2)
    else:
        return (x2, y2, x1, y1)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


len1 = line_length(x1, y1, x2, y2)
len2 = line_length(x3, y3, x4, y4)


if len1 >= len2:
    a1, b1, a2, b2 = x1, y1, x2, y2
else:
    a1, b1, a2, b2 = x3, y3, x4, y4

a1, b1, a2, b2 = closer_point(a1, b1, a2, b2)

# floor and print
a1 = math.floor(a1)
b1 = math.floor(b1)
a2 = math.floor(a2)
b2 = math.floor(b2)

print(f"({a1}, {b1})({a2}, {b2})")