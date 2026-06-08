n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

total_sum = 0

for i in range(1, n + 1):
    m = int(input())
    if m <= 5:
        total_sum += m
        p1 += m
    elif 6 <= m <= 12:
        total_sum += m
        p2 += m
    elif 13 <= m <= 25:
        total_sum += m
        p3 += m
    elif 26 <= m <= 40:
        total_sum += m
        p4 += m
    elif m >= 41:
        total_sum += m
        p5 += m

print(f'{p1 / total_sum * 100:.2f}%')
print(f'{p2 / total_sum * 100:.2f}%')
print(f'{p3 / total_sum * 100:.2f}%')
print(f'{p4 / total_sum * 100:.2f}%')
print(f'{p5 / total_sum * 100:.2f}%')
