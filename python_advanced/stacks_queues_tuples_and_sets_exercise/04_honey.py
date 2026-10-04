from collections import deque

bees = deque(list(map(int, input().split())))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
count = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        current_bee = bees.popleft()
        current_nectar = nectar.pop()
        symbol = symbols.popleft()

        if symbol == "+":
            count += abs(current_bee + current_nectar)
        elif symbol == "-":
            count += abs(current_bee - current_nectar)
        elif symbol == "*":
            count += abs(current_bee * current_nectar)
        elif symbol == "/":
            if current_nectar != 0:
                count += abs(current_bee / current_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {count}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}" )
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}" )
