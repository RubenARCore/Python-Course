substrings = input().split()

MAIN_COLORS = {"red", "yellow", "blue"}
SECONDARY_COLORS = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"}
}

ALL_VALID_COLORS = MAIN_COLORS.union(SECONDARY_COLORS.keys())

found_colors = []

while substrings:
    first = substrings[0]
    last = substrings[-1] if len(substrings) > 1 else ""

    if len(substrings) == 1:
        comb1 = first
        comb2 = ""
    else:
        comb1 = first + last
        comb2 = last + first

    matched_color = None
    if comb1 in ALL_VALID_COLORS:
        matched_color = comb1
    elif comb2 in ALL_VALID_COLORS:
        matched_color = comb2

    if matched_color:
        found_colors.append(matched_color)
        if len(substrings) == 1:
            substrings.pop(0)
        else:
            substrings.pop(0)
            substrings.pop(-1)
    else:
        first = first[:-1]
        if len(substrings) > 1:
            last = last[:-1]
            substrings.pop(0)
            substrings.pop(-1)
        else:
            substrings.pop(0)

        middle_idx = len(substrings) // 2

        if last:
            substrings.insert(middle_idx, last)
        if first:
            substrings.insert(middle_idx, first)

final_colors = []
for color in found_colors:
    if color in MAIN_COLORS:
        final_colors.append(color)
    elif color in SECONDARY_COLORS:
        required_mains = SECONDARY_COLORS[color]
        if required_mains.issubset(set(found_colors)):
            final_colors.append(color)

print(final_colors)