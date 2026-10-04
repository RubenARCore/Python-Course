n = int(input())
matrix = []
checker = True
for _ in range(n):
    matrix.append([x for x in input()])
data = input()

for row in range(n):
    if data in matrix[row]:
        print(f"({row}, {matrix[row].index(data)})")
        checker = False
        break
if checker:
    print(f"{data} does not occur in the matrix")
