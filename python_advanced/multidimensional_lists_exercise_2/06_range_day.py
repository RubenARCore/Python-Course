matrix = [input().split() for _ in range(5)]
target_count = 0
position = []

for row_idx, row in enumerate(matrix):
    if "A" in row:
        position = [row_idx, row.index("A")]
        break

target_count = sum(target_row.count("x") for target_row in matrix)

n = int(input())

for i in range(n):
    data = input().split()
    if data[0] == "move":
        steps = data[2]

        if data[1] == "right":
            pass
        elif data[1] == "left":
            pass
        elif data[1] == "up":
            pass
        elif data[1] == "down":
            pass
    else:
        if data[1] == "right":
            pass
        elif data[1] == "left":
            pass
        elif data[1] == "up":
            pass
        elif data[1] == "down":
            pass

