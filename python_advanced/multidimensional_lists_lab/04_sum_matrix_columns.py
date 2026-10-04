rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for j in range(rows):
    matrix.append([int(number) for number in input().split()])

for i in range(cols):
    result = 0

    for j in range(rows):
        result += matrix[j][i]
    print(result)