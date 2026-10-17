from collections import deque

checker = False
lo_checker = True

substances = list(map(int, input().split(", ")))
levels_of_energy = deque(map(int, input().split(", ")))

info_potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70,
}

crafted_potions = {}

while True:
    if len(crafted_potions) == 5 or len(substances) == 0 or len(levels_of_energy) == 0:
        if len(crafted_potions) == 5:
            checker = True
        break

    result = substances[-1] + levels_of_energy[0]


    for i in info_potions:
        if info_potions[i] == result:
            crafted_potions[i] = info_potions[i]
            del info_potions[i]
            substances.pop()
            levels_of_energy.popleft()
            lo_checker = False
            break
        elif result > info_potions[i]:
            crafted_potions[i] = info_potions[i]
            del info_potions[i]
            substances.pop()
            levels_of_energy.append(levels_of_energy.popleft() - 20)
            if levels_of_energy[-1] <= 0:
                levels_of_energy.pop()
            lo_checker = False
            break

    if lo_checker:
        substances.pop()
        levels_of_energy.append(levels_of_energy.popleft() - 5)
        if levels_of_energy[-1] <= 0:
            levels_of_energy.pop()
    lo_checker = True
    result = 0

if checker:
    print(f"Success! The alchemist has forged all potions!")
else:
    print(f"The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions.keys())}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")
if levels_of_energy:
    print(f"Crystals: {', '.join(map(str, levels_of_energy))}")
