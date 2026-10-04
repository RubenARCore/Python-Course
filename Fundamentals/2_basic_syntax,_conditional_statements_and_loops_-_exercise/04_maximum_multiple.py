n = int(input())
m = int(input())

for i in range(m, 1, - 1):
    if i % n == 0:
        print(i)
        exit()