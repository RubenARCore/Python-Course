f = int(input())
r = int(input())

for l in range(0, r):
    print(f'L{f}{l}', end=" ")

for r1 in range(f-1, 0, -1):
    print()
    for f1 in range(0,r):
        if r1 % 2 == 0:
            print(f'O{r1}{f1}', end=" ")
        else:
            print(f'A{r1}{f1}', end=" ")