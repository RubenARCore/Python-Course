from collections import deque

chocolate = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))

count = 0

while True:
    if len(chocolate) == 0 or len(milk) == 0:
        break

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        count += 1
        chocolate.pop()
        milk.popleft()
    else:
        milk.append(milk.popleft())
        chocolate[-1] -= 5

    if count == 5:
        break

if count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")

if len(milk) > 0:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")