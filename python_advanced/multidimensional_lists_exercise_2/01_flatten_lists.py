data = input().split("|")
result = []

for item in data[::-1]:
    result.extend(item.split())

print(*result, sep=" ")
