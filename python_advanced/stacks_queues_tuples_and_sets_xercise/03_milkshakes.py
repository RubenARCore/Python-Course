from collections import deque

chocolate = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))

count = 0

while True:
    while chocolate and chocolate[-1] <= 0:
        chocolate.pop()

    while milk and milk[0] <= 0:
        milk.popleft()

    if not chocolate or not milk:
        break

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

if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")