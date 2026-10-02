from collections import deque

bees = deque(list(map(int, input().split())))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
count = 0

while bees and nectar:
    if nectar[-1] > bees[0]:
        if symbols == "/" and nectar == 0:
            nectar.pop()
            symbols.popleft()
            bees.popleft()
        else:
            count += abs(eval(f"{nectar.pop()}{symbols.popleft()}{bees.popleft()}"))
    else:
        nectar.pop()

print(f"Total honey made: {count}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}" )
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}" )
