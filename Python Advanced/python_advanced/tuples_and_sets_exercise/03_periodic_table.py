n = int(input())

result = set()

for _ in range(n):
    data = input().split()
    for item in data:
        result.add(item)

print("\n".join(result))