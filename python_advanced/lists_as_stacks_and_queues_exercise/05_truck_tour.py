from collections import deque

pumps = deque()
n = int(input())
tank = 0
starting_point_counter = 0
length_counter = 0

for i in range(n):
    data = list(map(int, input().split()))
    pumps.append(data)

while True:
    tank += pumps[length_counter][0]
    if tank >= pumps[length_counter][1]:
        tank -= pumps[length_counter][1]
        length_counter += 1
        if length_counter == len(pumps):
            break
        continue
    else:
        pumps.append(pumps.popleft())
        starting_point_counter += 1
        length_counter = 0
        tank = 0
print(starting_point_counter)
