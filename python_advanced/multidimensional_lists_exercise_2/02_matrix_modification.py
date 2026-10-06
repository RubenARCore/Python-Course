n = int(input())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

while True:
    data = input().split(" ", 1)
    if data[0] == "END":
        break
    coordinates = list(map(int, data[1].split()))
    r, c, value = coordinates

    if 0 <= r < n and 0 <= c < n:
        if data[0] == "Add":
            matrix[r][c] += value

        else:
            matrix[r][c] -= value
    else:
        print(f"Invalid coordinates")

for item in matrix:
    print(*item, sep=" ")