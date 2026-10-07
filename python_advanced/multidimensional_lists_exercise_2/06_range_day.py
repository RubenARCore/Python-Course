matrix = [input().split() for _ in range(5)]
target_count = 0
position = []
shot_target_position = []

checker = True
for row_idx, row in enumerate(matrix):
    if "A" in row:
        position = [row_idx, row.index("A")]
        break

pr, pc = position

target_count = sum(target_row.count("x") for target_row in matrix)
final_target = target_count
n = int(input())

for i in range(n):

    data = input().split()

    if data[0] == "move":
        checker = True
        steps = int(data[2])

        if data[1] == "right" and 0 <= pc + steps < 5:
            for s in range(1, steps + 1):
                if matrix[pr][pc + s] == ".":
                    checker = True
                else:
                    checker = False
                    break

            if checker:
                matrix[pr][pc] = "."
                matrix[pr][pc + steps] = "A"
                pc += steps

        elif data[1] == "left" and 0 <= pc - steps < 5:
            for s in range(1, steps + 1):
                if matrix[pr][pc - s] == ".":
                    checker = True
                else:
                    checker = False
                    break

            if checker:
                matrix[pr][pc] = "."
                matrix[pr][pc - steps] = "A"
                pc -= steps

        elif data[1] == "up" and 0 <= pr - steps < 5:
            for s in range(1, steps + 1):
                if matrix[pr - s][pc] == ".":
                    checker = True
                else:
                    checker = False
                    break

            if checker:
                matrix[pr][pc] = "."
                matrix[pr - steps][pc] = "A"
                pr -= steps

        elif data[1] == "down" and 0 <= pr + steps < 5:
            for s in range(1, steps + 1):
                if matrix[pr + s][pc] == ".":
                    checker = True
                else:
                    checker = False
                    break

            if checker:
                matrix[pr][pc] = "."
                matrix[pr + steps][pc] = "A"
                pr += steps

    else:
        if data[1] == "right":
            for h in range(1, 5 - pc):
                if matrix[pr][pc + h] == "x":
                    matrix[pr][pc + h] = "."
                    target_count -= 1
                    shot_target_position.append([pr, pc + h])
                    break

        elif data[1] == "left":
            for h in range(1, pc + 1):
                if matrix[pr][pc - h] == "x":
                    matrix[pr][pc - h] = "."
                    target_count -= 1
                    shot_target_position.append([pr, pc - h])
                    break

        elif data[1] == "up":
            for h in range(1, pr + 1):
                if matrix[pr - h][pc] == "x":
                    matrix[pr - h][pc] = "."
                    target_count -= 1
                    shot_target_position.append([pr - h, pc])
                    break

        elif data[1] == "down":
            for h in range(1, 5 - pr):
                if matrix[pr + h][pc] == "x":
                    matrix[pr + h][pc] = "."
                    target_count -= 1
                    shot_target_position.append([pr + h, pc])
                    break

    if target_count == 0:
        print(f"Training completed! All {final_target} targets hit.")

        for item in shot_target_position:
            print(item)

        exit()

print(f"Training not completed! {target_count} targets left.")

for item in shot_target_position:
    print(item)