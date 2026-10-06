n = int(input())
matrix = []
total_sum = 0

for i in range(n):
    matrix.append(list(input().split(" ")))

for row_idx, row in enumerate(matrix):
    if "A" in row:
        col_idx = row.index("A")
        alice = [row_idx, col_idx]
        break

ar, ac = alice

while True:
    command = input()

    if command == "up":
        if ar - 1 < 0:
            matrix[ar][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        elif matrix[ar - 1][ac] == "R":
            matrix[ar][ac] = "*"
            matrix[ar - 1][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        else:
            if matrix[ar - 1][ac].isdigit():
                total_sum += int(matrix[ar - 1][ac])

            matrix[ar][ac] = "*"
            matrix[ar - 1][ac] = "A"
            ar -= 1

    elif command == "left":
        if ac - 1 < 0:
            matrix[ar][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        elif matrix[ar][ac - 1] == "R":
            matrix[ar][ac] = "*"
            matrix[ar][ac - 1] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        else:
            if matrix[ar][ac - 1].isdigit():
                total_sum += int(matrix[ar][ac - 1])

            matrix[ar][ac] = "*"
            matrix[ar][ac - 1] = "A"
            ac -= 1

    elif command == "down":
        if ar + 1 >= n:
            matrix[ar][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        elif matrix[ar + 1][ac] == "R":
            matrix[ar][ac] = "*"
            matrix[ar + 1][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        else:
            if matrix[ar + 1][ac].isdigit():
                total_sum += int(matrix[ar + 1][ac])

            matrix[ar][ac] = "*"
            matrix[ar + 1][ac] = "A"
            ar += 1

    elif command == "right":
        if ac + 1 >= n:
            matrix[ar][ac] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        elif matrix[ar][ac + 1] == "R":
            matrix[ar][ac] = "*"
            matrix[ar][ac + 1] = "*"
            print(f"Alice didn't make it to the tea party.")
            for item in matrix:
                print(*item, sep=" ")
            break

        else:
            if matrix[ar][ac + 1].isdigit():
                total_sum += int(matrix[ar][ac + 1])

            matrix[ar][ac] = "*"
            matrix[ar][ac + 1] = "A"
            ac += 1

    if total_sum >= 10:
        matrix[ar][ac] = "*"
        print(f"She did it! She went to the party.")
        for item in matrix:
            print(*item, sep=" ")
        break