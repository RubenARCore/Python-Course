n = int(input())
matrix = []
sum_number = 0

for i in range(n):
    matrix.extend(list(map(int, input().split())))

for i in range(0, n*n, n+1):
    sum_number += matrix[i]

print(sum_number)