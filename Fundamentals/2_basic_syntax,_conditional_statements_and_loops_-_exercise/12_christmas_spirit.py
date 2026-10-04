quantity = int(input())
days = int(input())

cost = 0
spirit = 0

for day in range(1, days + 1):

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        cost += quantity * 2
        spirit += 5

    if day % 3 == 0:
        cost += quantity * (5 + 3)
        spirit += 3 + 10

    if day % 5 == 0:
        cost += quantity * 15
        spirit += 17

    if day % 15 == 0:
        spirit += 30

    if day % 10 == 0:
        spirit -= 20

        # cat ruins → buy 1 of each (NOT quantity)
        cost += 5 + 3 + 15

    if day == days and day % 10 == 0:
        spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")