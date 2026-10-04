import sys

sys.setrecursionlimit(2000)

n = int(input())
board = []

for _ in range(n):
    row = input().replace('–', '-').split()
    board.append(row)

max_dots = 0
cols = len(board[0]) if n > 0 else 0


def dfs(r, c):
    if r < 0 or r >= n or c < 0 or c >= cols or board[r][c] != '.':
        return 0

    board[r][c] = '-'

    count = 1
    count += dfs(r - 1, c)
    count += dfs(r + 1, c)
    count += dfs(r, c - 1)
    count += dfs(r, c + 1)

    return count


for r in range(n):
    for c in range(cols):
        if board[r][c] == '.':
            current_connected_dots = dfs(r, c)
            if current_connected_dots > max_dots:
                max_dots = current_connected_dots

print(max_dots)