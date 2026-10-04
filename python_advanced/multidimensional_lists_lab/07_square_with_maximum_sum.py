rows, cols = list(map(int, input().split(", ")))
matrix = []
max_sum = float('-inf')
result_lst = []
for _ in range(rows):
    matrix.append(list(map(int, input().split(", "))))

for j in range(0, rows-1):
    for i in range(0, cols-1):
        first = matrix[j][i]
        second = matrix[j][i + 1]
        third = matrix[j + 1][i]
        fourth = matrix[j + 1][i+1]
        if max_sum < (first + second+third+fourth):
            max_sum = first + second+third+fourth
            result_lst.clear()
            result_lst.append([matrix[j][i], matrix[j][i + 1]])
            result_lst.append([matrix[j + 1][i], matrix[j + 1][i+1]])

for item in result_lst:
    print(*item, sep=" ")
print(max_sum)