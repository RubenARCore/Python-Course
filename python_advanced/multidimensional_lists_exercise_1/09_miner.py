size = int(input())
commands = input().split()

field = []
miner_row = 0
miner_col = 0
coal = 0

for row in range(size):
    data = input().split()
    field.append(data)

    for col in range(size):
        if data[col] == "s":
            miner_row = row
            miner_col = col
        elif data[col] == "c":
            coal += 1

for command in commands:
    if command == "left":
        if miner_col > 0:
            miner_col -= 1
    elif command == "right":
        if miner_col < size - 1:
            miner_col += 1
    elif command == "up":
        if miner_row > 0:
            miner_row -= 1
    elif command == "down":
        if miner_row < size - 1:
            miner_row += 1

    if field[miner_row][miner_col] == "c":
        field[miner_row][miner_col] = "*"
        coal -= 1

    if coal == 0:
        print(f"You collected all coal! ({miner_row}, {miner_col})")
        break

    if field[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        break
else:
    print(f"{coal} pieces of coal left. ({miner_row}, {miner_col})")