data = list(map(int, input().split()))

result = []

while data:
    result.append(str(data.pop()))

print(" ".join(result))