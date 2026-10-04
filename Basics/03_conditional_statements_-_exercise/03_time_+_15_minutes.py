import math

hours = int(input())
minutes = int(input())

total_time = hours * 60 + minutes + 15

hours = total_time / 60
hours = math.trunc(hours)
minutes = total_time % 60

if hours >= 24:
    hours = hours - 24

print(f'{hours}:{minutes:02d}')