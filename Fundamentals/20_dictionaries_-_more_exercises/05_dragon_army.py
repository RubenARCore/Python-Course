id="5n9h4p"
from collections import OrderedDict

dragons = OrderedDict()

n = int(input())

for _ in range(n):
    data = input().split()

    dragon_type = data[0]
    name = data[1]

    damage = data[2]
    health = data[3]
    armor = data[4]

    if damage == "null":
        damage = 45
    else:
        damage = int(damage)

    if health == "null":
        health = 250
    else:
        health = int(health)

    if armor == "null":
        armor = 10
    else:
        armor = int(armor)

    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][name] = {
        "damage": damage,
        "health": health,
        "armor": armor
    }


for dragon_type, dragon_data in dragons.items():

    count = len(dragon_data)

    total_damage = 0
    total_health = 0
    total_armor = 0

    for dragon in dragon_data.values():
        total_damage += dragon["damage"]
        total_health += dragon["health"]
        total_armor += dragon["armor"]

    avg_damage = total_damage / count
    avg_health = total_health / count
    avg_armor = total_armor / count

    print(
        f"{dragon_type}::"
        f"({avg_damage:.2f}/"
        f"{avg_health:.2f}/"
        f"{avg_armor:.2f})"
    )

    for name in sorted(dragon_data):
        dragon = dragon_data[name]

        print(
            f"-{name} -> "
            f"damage: {dragon['damage']}, "
            f"health: {dragon['health']}, "
            f"armor: {dragon['armor']}"
        )