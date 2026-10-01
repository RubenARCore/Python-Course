n = int(input())
guests_list = set()
vips = []
losers = []
arrived = set()

for _ in range(n):
    guests_list.add(input())

for guest in guests_list:
    if guest[0].isdigit():
        vips.append(guest)
    else:
        losers.append(guest)

while True:
    data = input()

    if data == "END":
        break

    arrived.add(data)

print(len(arrived) - (len(losers) - len(vips)))

result_vips = list((set(vips)).difference(arrived))
result_losers = list((set(losers)).difference(arrived))
result_losers.reverse()


for guest in result_vips:
    print(guest)

for guest in result_losers:
    print(guest)
