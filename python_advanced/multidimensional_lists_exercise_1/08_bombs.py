n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

bombs_input = input().split()

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for bomb in bombs_input:
    r, c = map(int, bomb.split(","))

    if matrix[r][c] > 0:
        power = matrix[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] > 0:
                matrix[nr][nc] -= power

        matrix[r][c] = 0

alive_cells = 0
sum_of_cells = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_of_cells += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")

for row in matrix:
    print(*row)