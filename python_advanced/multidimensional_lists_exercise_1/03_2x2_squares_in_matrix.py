rows, cols = list(map(int, input().split()))
matrix = []
count = 0
for _ in range(rows):
    matrix.append(input().split())

for j in range(0, rows-1):
    for i in range(0, cols-1):
        first = matrix[j][i]
        second = matrix[j][i + 1]
        third = matrix[j + 1][i]
        fourth = matrix[j + 1][i+1]

        if first == second == third == fourth:
            count += 1

print(count)