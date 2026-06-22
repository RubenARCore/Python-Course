n = list(map(int, input().split(".")))

for i in range(2, -1, -1):
    n[i] += 1
    if n[i] <= 9:
        break
    n[i] = 0

print(f"{n[0]}.{n[1]}.{n[2]}")