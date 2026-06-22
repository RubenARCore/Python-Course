n = list(map(int, input().split(", ")))

lst = [m for m in range(len(n)) if n[m] % 2 == 0]

print(lst)