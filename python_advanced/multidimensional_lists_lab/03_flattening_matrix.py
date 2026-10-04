n = int(input())
matrix = []

for _ in range(n):
    data = list(map(int, input().split(", ")))
    matrix.extend(data)

print(matrix)
