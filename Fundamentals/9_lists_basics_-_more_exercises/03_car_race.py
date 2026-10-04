n = list(map(int, input().split()))
left_car = []
right_car = []
sum_left = 0
sum_right = 0


for i in range(len(n) // 2):
    left_car.append(n[i])
    right_car.append(n[len(n) - 1 - i])

for i in range(len(left_car)):

    if left_car[i] == 0:
        sum_left *= 0.8

    sum_left += left_car[i]

for i in range(len(right_car)):
    if right_car[i] == 0:
        sum_right *= 0.8

    sum_right += right_car[i]

if sum_left > sum_right:
    print(f'The winner is right with total time: {sum_right:.1f}')
else:
    print(f'The winner is left with total time: {sum_left:.1f}')
