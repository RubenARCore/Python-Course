presents = int(input())
n = int(input())

neighborhood = [input().split() for _ in range(n)]

santa_row = 0
santa_col = 0
nice_kids = 0

for row_idx, row in enumerate(neighborhood):
    nice_kids += row.count("V")

    if "S" in row:
        santa_row = row_idx
        santa_col = row.index("S")

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

happy_nice_kids = 0

while True:
    command = input()

    if command == "Christmas morning":
        break

    row_change, col_change = commands[command]

    new_row = santa_row + row_change
    new_col = santa_col + col_change

    neighborhood[santa_row][santa_col] = "-"

    santa_row = new_row
    santa_col = new_col

    if neighborhood[santa_row][santa_col] == "V":
        neighborhood[santa_row][santa_col] = "-"
        presents -= 1
        happy_nice_kids += 1

    elif neighborhood[santa_row][santa_col] == "X":
        neighborhood[santa_row][santa_col] = "-"

    elif neighborhood[santa_row][santa_col] == "C":
        neighborhood[santa_row][santa_col] = "-"

        for row_change, col_change in commands.values():
            current_row = santa_row + row_change
            current_col = santa_col + col_change

            if neighborhood[current_row][current_col] == "V":
                neighborhood[current_row][current_col] = "-"
                presents -= 1
                happy_nice_kids += 1

            elif neighborhood[current_row][current_col] == "X":
                neighborhood[current_row][current_col] = "-"
                presents -= 1

        santa_row = new_row
        santa_col = new_col

    if presents == 0:
        break

neighborhood[santa_row][santa_col] = "S"

remaining_nice_kids = nice_kids - happy_nice_kids

if presents == 0 and remaining_nice_kids > 0:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(" ".join(row))

if remaining_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {remaining_nice_kids} nice kid/s.")