from datetime import timedelta, datetime
from collections import deque

data = input().replace(";", "-").split("-")

names = []
times = []

for i in range(0, len(data), 2):
    names.append(data[i])
    times.append(int(data[i + 1]))


starting_time = list(map(int, input().split(":")))
hours, minutes, seconds = starting_time

t = datetime(2026, 1, 1, hours, minutes, seconds)


products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)


free_at = [t for _ in names]


while products:

    t += timedelta(seconds=1)

    product = products.popleft()

    robot_found = False

    for i in range(len(names)):

        if free_at[i] <= t:

            print(
                f"{names[i]} - {product} "
                f"[{t.strftime('%H:%M:%S')}]"
            )

            free_at[i] = t + timedelta(seconds=times[i])

            robot_found = True
            break

    if not robot_found:
        products.append(product)