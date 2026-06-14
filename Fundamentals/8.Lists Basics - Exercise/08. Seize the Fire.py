fire_input = input().split("#")
water = int(input())

ranges = {
    "High": (81, 125),
    "Medium": (51, 80),
    "Low": (1, 50)
}

cells = []
total_fire = 0
effort = 0

for item in fire_input:
    parts = item.split(" = ")
    fire_type = parts[0]
    value = int(parts[1])

    min_val, max_val = ranges[fire_type]

    if not (min_val <= value <= max_val):
        continue

    if water < value:
        continue

    water -= value
    cells.append(value)
    total_fire += value
    effort += value * 0.25

print("Cells:")
for c in cells:
    print(f" - {c}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")