n = int(input())
matrix = []
reversed_matrix = []
temporary_matrix = []
sum_number = 0
result_lst = []

for i in range(n):
    temporary_matrix = list(map(int, input().split(", ")))
    matrix.extend(temporary_matrix)
    reversed_matrix.extend(temporary_matrix[::-1])

for i in range(0, n*n, n+1):
    sum_number += matrix[i]
    result_lst.append(matrix[i])

print(f"Primary diagonal: {', '.join(map(str, result_lst))}. Sum: {sum_number}")

result_lst.clear()
sum_number = 0

for i in range(0, n*n, n+1):
    sum_number += reversed_matrix[i]
    result_lst.append(reversed_matrix[i])

print(f"Secondary diagonal: {', '.join(map(str, result_lst))}. Sum: {sum_number}")
