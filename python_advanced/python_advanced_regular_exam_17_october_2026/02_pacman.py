
n = int(input())
matrix = []
star_sum = 0
health = 100
immunity = False

for i in range(n):
    matrix.append(list(input()))

for row_idx, row in enumerate(matrix):
    if 'P' in row:
        col_idx = row.index('P')
        pacman = [row_idx, col_idx]
        break

prow, pcol = pacman

for row in matrix:
    star_sum += row.count("*")

while True:
    if health <= 0 or star_sum == 0:
        break

    command = input()
    if command == "end":
        break

    if command == "up":
        new_prow = (prow - 1) % n

        if matrix[new_prow][pcol] == "*":
            star_sum -= 1
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "-":
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "G":
            if immunity:
                immunity = False
            else:
                health -= 50
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "F":
            immunity = True
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

    elif command == "down":
        new_prow = (prow + 1) % n

        if matrix[new_prow][pcol] == "*":
            star_sum -= 1
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "-":
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "G":
            if immunity:
                immunity = False
            else:
                health -= 50
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

        elif matrix[new_prow][pcol] == "F":
            immunity = True
            matrix[new_prow][pcol] = "P"
            matrix[prow][pcol] = "-"
            prow = new_prow

    elif command == "left":
        new_pcol = (pcol - 1) % n

        if matrix[prow][new_pcol] == "*":
            star_sum -= 1
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "-":
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "G":
            if immunity:
                immunity = False
            else:
                health -= 50
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "F":
            immunity = True
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

    elif command == "right":
        new_pcol = (pcol + 1) % n

        if matrix[prow][new_pcol] == "*":
            star_sum -= 1
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "-":
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "G":
            if immunity:
                immunity = False
            else:
                health -= 50
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

        elif matrix[prow][new_pcol] == "F":
            immunity = True
            matrix[prow][new_pcol] = "P"
            matrix[prow][pcol] = "-"
            pcol = new_pcol

if health <= 0:
    print(f"Game over! Pacman last coordinates [{prow},{pcol}]")
elif star_sum == 0:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if star_sum > 0:
    print(f"Uncollected stars: {star_sum}")

for row in matrix:
    print(*row, sep="")
