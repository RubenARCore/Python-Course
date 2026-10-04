n = int(input())
rows = []
start = None

for i in range(n):
    row = list(input())
    if 'k' in row:
        start = (i, row.index('k'))
    rows.append(row)

max_moves = -1
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(r, c, steps):
    global max_moves


    if r == 0 or c == 0 or r == n - 1 or c == len(rows[r]) - 1:
        max_moves = max(max_moves, steps)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if 0 <= nr < n and 0 <= nc < len(rows[nr]):

            if rows[nr][nc] == ' ':
                rows[nr][nc] = 'v'
                dfs(nr, nc, steps + 1)
                rows[nr][nc] = ' '


sr, sc = start
rows[sr][sc] = 'v'
dfs(sr, sc, 1)

if max_moves == -1:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {max_moves} moves")

    # Взаимствано решение 