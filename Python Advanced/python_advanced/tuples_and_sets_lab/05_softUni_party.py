n = int(input())
vips = set()
losers = set()
for _ in range(n):
    reservation = input()
    if reservation[0].isdigit():
        vips.add(reservation)
    else:
        losers.add(reservation)

while True:
    guest = input()
    if guest in vips:
