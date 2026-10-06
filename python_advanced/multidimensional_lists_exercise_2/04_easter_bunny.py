n = int(input())

matrix = []
bunny_position = []
direction = ""
direction_steps = []
current_steps = []
eggs = float("-inf")
current_eggs = 0

matrix = [input().split() for _ in range(n)]

for row_idx, row in enumerate(matrix):
    if "B" in row:
        col_idx = row.index("B")
        bunny_position = [row_idx, col_idx]
        break

br, bc = bunny_position

for a in range(n):

    if 0 <= bc + a + 1 < n:
        if matrix[br][bc + a + 1] == "X":
            break

        current_eggs += int(matrix[br][bc + a + 1])
        current_steps.append([br, bc + a + 1])

if current_eggs > eggs:
    eggs = current_eggs
    direction_steps = current_steps.copy()
    direction = "right"

current_eggs = 0
current_steps.clear()

for a in range(n):

    if 0 <= bc - a - 1 < n:
        if matrix[br][bc - a - 1] == "X":
            break

        current_eggs += int(matrix[br][bc - a - 1])
        current_steps.append([br, bc - a - 1])

if current_eggs > eggs:
    eggs = current_eggs
    direction_steps = current_steps.copy()
    direction = "left"

current_eggs = 0
current_steps.clear()

for a in range(n):

    if 0 <= br - a - 1 < n:
        if matrix[br - a - 1][bc] == "X":
            break

        current_eggs += int(matrix[br - a - 1][bc])
        current_steps.append([br - a - 1, bc])

if current_eggs > eggs:
    eggs = current_eggs
    direction_steps = current_steps.copy()
    direction = "up"

current_eggs = 0
current_steps.clear()

for a in range(n):

    if 0 <= br + a + 1 < n:
        if matrix[br + a + 1][bc] == "X":
            break

        current_eggs += int(matrix[br + a + 1][bc])
        current_steps.append([br + a + 1, bc])

if current_eggs > eggs:
    eggs = current_eggs
    direction_steps = current_steps.copy()
    direction = "down"

current_eggs = 0
current_steps.clear()


print(direction)
for item in direction_steps:
    print(item)

print(eggs)
