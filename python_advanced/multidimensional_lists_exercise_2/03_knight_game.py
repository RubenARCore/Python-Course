n = int(input())

matrix = []
for _ in range(n):
    row = list(input())
    matrix.append(row)

d_row = [-2, -2, -1, -1,  1,  1,  2,  2]
d_col = [-1,  1, -2,  2, -2,  2, -1,  1]

removed_knights = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 'K':
                current_attacks = 0

                for i in range(8):
                    next_r = r + d_row[i]
                    next_c = c + d_col[i]

                    if 0 <= next_r < n and 0 <= next_c < n:
                        if matrix[next_r][next_c] == 'K':
                            current_attacks += 1

                if current_attacks > max_attacks:
                    max_attacks = current_attacks
                    knight_to_remove = (r, c)

    if max_attacks == 0:
        break


    rem_r, rem_c = knight_to_remove
    matrix[rem_r][rem_c] = '0'
    removed_knights += 1

print(removed_knights)