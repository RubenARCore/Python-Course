n = int(input())

for i in range(1, n + 1):
    data = int(input())

    if data % 2 != 0:
        print(f'{data} is odd!')
        exit(0)

print(f'All numbers are even.')