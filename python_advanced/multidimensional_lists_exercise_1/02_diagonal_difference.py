n = int(input())
matrix = []
reversed_matrix = []
temporary_matrix = []
sum_first = 0
sum_second = 0
result_lst = []

for i in range(n):
    temporary_matrix = list(map(int, input().split()))
    matrix.extend(temporary_matrix)
    reversed_matrix.extend(temporary_matrix[::-1])

for i in range(0, n*n, n+1):
    sum_first += matrix[i]
    result_lst.append(matrix[i])

result_lst.clear()

for i in range(0, n*n, n+1):
    sum_second += reversed_matrix[i]
    result_lst.append(reversed_matrix[i])

print(f"{abs(sum_first - sum_second)}")
