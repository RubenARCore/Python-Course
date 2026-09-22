from collections import deque

deque = deque()

dispenser = int(input())

while True:
    name_data = input()
    if name_data == 'Start':
        break
    deque.append(name_data)

while True:
    command = input().split()

    if command[0] == 'End':
        break
    elif command[0] == 'refill':
        dispenser += int(command[1])
        continue

    if int(command[0]) <= dispenser:
        print(f"{deque.popleft()} got water")
        dispenser -= int(command[0])
    else:
        print(f"{deque.popleft()} must wait")

print(f"{dispenser} liters left")
