from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

target_crafts = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while materials and magic:
    curr_material = materials[-1]
    curr_magic = magic[0]

    if curr_material == 0 or curr_magic == 0:
        if curr_material == 0:
            materials.pop()
        if curr_magic == 0:
            magic.popleft()
        continue

    product = curr_material * curr_magic

    if product in target_crafts:
        present_name = target_crafts[product]
        crafted_presents[present_name] = crafted_presents.get(present_name, 0) + 1
        materials.pop()
        magic.popleft()

    elif product < 0:
        total_sum = curr_material + curr_magic
        materials.pop()
        magic.popleft()
        materials.append(total_sum)

    elif product > 0:
        magic.popleft()
        materials[-1] += 15

has_doll_and_train = crafted_presents.get("Doll", 0) > 0 and crafted_presents.get("Wooden train", 0) > 0
has_bear_and_bike = crafted_presents.get("Teddy bear", 0) > 0 and crafted_presents.get("Bicycle", 0) > 0

if has_doll_and_train or has_bear_and_bike:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")