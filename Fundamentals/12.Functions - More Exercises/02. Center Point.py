numbers = [float(input()) for _ in range(4)]

def center_point(point):
    x1, y1, x2, y2 = point

    distance1 = x1 ** 2 + y1 ** 2
    distance2 = x2 ** 2 + y2 ** 2

    if distance1 <= distance2:
        return [int(x1), int(y1)]

    return [int(x2), int(y2)]

print(f'({", ".join(map(str, center_point(numbers)))})')