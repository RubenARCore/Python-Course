n = int(input())
m = int(input())
k = int(input())

counter = 0

for i in range(n, m + 1):
    for j in range(n, m + 1):
        counter += 1

        if i + j == k:
            print(f'Combination N:{counter} ({i} + {j} = {i + j})')
            exit()

print(f'{counter} combinations - neither equals {k}')