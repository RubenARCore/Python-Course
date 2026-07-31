n = int(input())

plants = {}

for i in range(n):
    data = input().split("<->")

    name = data[0]
    rarity = int(data[1])

    if name not in plants:
        plants[name] = {"rarity": rarity,"ratings": []}
    else:
        plants[name]["rarity"] = rarity

while True:
    data = input()
    if data == "Exhibition":
        break

    data = data.split(":")

    if data[0] == "Rate":
        data = data[1].split(" - ")
        name = data[0].strip()
        rating = int(data[1])
        plants[name]["ratings"].append(rating)

    elif data[0] == "Update":
        data = data[1].split(" - ")
        name = data[0].strip()
        rarity = int(data[1])
        plants[name]["rarity"] = rarity

    elif data[0] == "Reset":
        data = data[1].split(" - ")
        name = data[0].strip()
        plants[name]["ratings"].clear()

print("Plants for the exhibition:")


for name, data in plants.items():
    rating = sum(data["ratings"]) / (len(data["ratings"]) or 1)
    print(f"- {name}; Rarity: {data['rarity']}; Rating: {rating:.2f}")