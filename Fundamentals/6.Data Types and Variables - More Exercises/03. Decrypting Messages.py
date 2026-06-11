key = int(input())
n = int(input())

for i in range(1, n + 1):
    data = input()
    print(f'{chr(ord(data) + key)}', end='')
