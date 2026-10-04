n = int(input())

guests = set()

for _ in range(n):
    guests.add(input())

while True:
    guest = input()

    if guest == "END":
        break

    guests.remove(guest)

vips = sorted([guest for guest in guests if guest[0].isdigit()])
regular = sorted([guest for guest in guests if not guest[0].isdigit()])

print(len(guests))

for guest in vips:
    print(guest)

for guest in regular:
    print(guest)