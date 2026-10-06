rows, cols = map(int, input().split())

lair = []
player_row = 0
player_col = 0
bunnies = set()

for r in range(rows):
    row_data = list(input())
    for c in range(cols):
        if row_data[c] == "P":
            player_row = r
            player_col = c
        elif row_data[c] == "B":
            bunnies.add((r, c))
    lair.append(row_data)

commands = input()

has_escaped = False
is_dead = False

for command in commands:
    new_row = player_row
    new_col = player_col

    if command == "L":
        new_col -= 1
    elif command == "R":
        new_col += 1
    elif command == "U":
        new_row -= 1
    elif command == "D":
        new_row += 1

    lair[player_row][player_col] = "."

    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
        has_escaped = True
    else:
        player_row = new_row
        player_col = new_col

        if lair[player_row][player_col] == "B":
            is_dead = True
        else:
            lair[player_row][player_col] = "P"

    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies:
        for dr, dc in directions:
            nr, nc = b_row + dr, b_col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_bunnies.add((nr, nc))
                lair[nr][nc] = "B"

    bunnies.update(new_bunnies)

    if not has_escaped and (player_row, player_col) in bunnies:
        is_dead = True

    if has_escaped or is_dead:
        break

for row in lair:
    print("".join(row))

if has_escaped:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")