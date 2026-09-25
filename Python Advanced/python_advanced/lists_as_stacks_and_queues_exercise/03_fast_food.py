from collections import deque

quantity_of_food  = int(input())
orders = deque(list(map(int, input().split())))

print(max(orders))

while len(orders) and quantity_of_food >= orders[0]:

    quantity_of_food -= orders.popleft()

if len(orders) == 0:
    print("Orders complete")
else:
    orders_left = " ".join(str(x) for x in orders)
    print(f"Orders left: {orders_left}")
