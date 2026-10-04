n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(number) for number in input().split(", ") if int(number) % 2 == 0])

print(matrix)