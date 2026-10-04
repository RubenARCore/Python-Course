dwarfs = {}

while True:
    command = input()

    if command == "Once upon a time":
        break

    name, color, physics = command.split(" <:> ")
    physics = int(physics)

    if color not in dwarfs:
        dwarfs[color] = {}

    if name not in dwarfs[color]:
        dwarfs[color][name] = physics

    else:
        if physics > dwarfs[color][name]:
            dwarfs[color][name] = physics


color_count = {}

for color in dwarfs:
    color_count[color] = len(dwarfs[color])

result = []

for color in dwarfs:
    for name in dwarfs[color]:
        physics = dwarfs[color][name]

        result.append(
            {
                "name": name,
                "color": color,
                "physics": physics,
                "count": color_count[color]
            }
        )

result.sort(
    key=lambda dwarf: (
        -dwarf["physics"],
        -dwarf["count"]
    )
)

for dwarf in result:
    print(
        f"({dwarf['color']}) "
        f"{dwarf['name']} <-> "
        f"{dwarf['physics']}"
    )