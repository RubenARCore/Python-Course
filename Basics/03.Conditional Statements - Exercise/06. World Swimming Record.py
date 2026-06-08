import math

seconds = float(input())
meters = float(input())
seconds_per_meter = float(input())

time = meters * seconds_per_meter
slowdown = math.floor(meters / 15) * 12.5
total_time = time + slowdown

if total_time >= seconds:
    print(f'No, he failed! He was {math.fabs(seconds - total_time):.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
