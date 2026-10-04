rows, cols = map(int, input().split(", "))
matrix = []
sum_number = 0

for _ in range(rows):
    matrix.append([int(number) for number in input().split(", ")])
    sum_number += sum(matrix[_])

print(sum_number)
print(matrix)