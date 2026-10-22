n = int(input())

for i in range(1, n):
    print(" " * (n - i), end="")
    for j in range(0, i):
        print("* ", end="")
    print()
print("* " * n)

for k in range(n-1, 0, -1):
    print(" " * (n - k), end="")
    for _ in range(0, k):
        print("* ", end="")
    print()