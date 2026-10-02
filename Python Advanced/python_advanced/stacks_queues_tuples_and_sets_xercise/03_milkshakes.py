from collections import deque

chocolate = list(map(int, input().split(", ")))
tuple(chocolate)
milk = list(map(int, input().split(", ")))
milk = deque(milk)

count = 0

while True:

    if chocolate[-1] <= 0:
        chocolate.pop()
    if milk[0] <= 0:
        milk.popleft()

    if len(chocolate) == 0:
        break
    if len(milk) == 0:
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

if len(chocolate) > 0:
    print(f"Chocolate: ", end="")
    print(*chocolate, sep=", ")
else:
    print(f"Chocolate: empty")

if len(milk) > 0:
    print(f"Milk: ", end="")
    print(*milk, sep=", ")
else:
    print(f"Milk: empty")