n = int(input())

in_parking = set()

for i in range(n):
    data = input().split(", ")
    if data[0] == "IN":
        in_parking.add(data[1])
    else:
        in_parking.remove(data[1])

if not in_parking:
    print("Parking Lot is Empty")
else:
    print("\n".join(in_parking))