n = list(input())
m = input()

current = n.copy()

for i in range(len(n)):
    if current[i] != m[i]:
        current[i] = m[i]
        print("".join(current))