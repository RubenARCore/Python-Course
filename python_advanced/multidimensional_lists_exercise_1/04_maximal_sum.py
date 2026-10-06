rows, cols = map(int, input().split())
matrix = [list(map(int,input().split())) for i in range(rows)]
result_sum = float('-inf')
result_lst = []
temporary_lst = []

for a in range(rows-2):
    for b in range(cols-2):
        result = 0
        temporary_lst.clear()

        for c in range(3):
            temporary_lst.append(matrix[c+a][b : 3+b])

        for item in temporary_lst:
            result += sum(item)

        if result > result_sum:
            result_sum = result
            result_lst = temporary_lst.copy()

print(f"Sum = {result_sum}")
[print(" ".join(map(str, item))) for item in result_lst]