rows, cols = map(int, input().split())

for i in range(rows):
    for j in range(cols):
        print(chr(97+i) + chr(97+j+i) + chr(97+i), end=" ")
    print()