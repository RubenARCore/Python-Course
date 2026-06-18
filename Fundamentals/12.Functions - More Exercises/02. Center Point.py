numbers = []
for _ in range(4):
    numbers.append(float(input()))

def center_point(point):
    x1, y1, x2, y2 = point

    d1 = x1 ** 2 + y1 ** 2
    d2 = x2 ** 2 + y2 ** 2

    if d1 <= d2:
        return [int(x1), int(y1)]
    else:
        return [int(x2), int(y2)]

result = center_point(numbers)
print(f'({", ".join(map(str, result))})')