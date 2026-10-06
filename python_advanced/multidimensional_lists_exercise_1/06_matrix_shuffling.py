rows, cols = map(int, input().split())
matrix = []


for i in range(rows):
    matrix.append(input().split())

while True:
    data = input().split(" ", 1)
    if data[0] == "END":
        break

    coordinates = data[1].split()

    if data[0] == "swap" and len(coordinates) == 4:
        row1, col1, row2, col2 = map(int, coordinates)

        if (0 <= row1 < rows and 0 <= col1 < cols) and (0 <= row2 < rows and 0 <= col2 < cols):
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

            for row in matrix:
                print(" ".join(map(str, row)))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")