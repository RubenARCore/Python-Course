data = input().split(", ")

data.sort(key=lambda x: (-len(x), x))

print(data)