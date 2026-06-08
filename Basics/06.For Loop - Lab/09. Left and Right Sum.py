import math

n = int(input())

left_sum = 0
right_sum = 0

for i in range(n):
    l = int(input())
    left_sum += l
for i in range(n):
    r = int(input())
    right_sum += r

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')