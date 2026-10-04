data = list(map(float, input().split()))
result = {}

for value in data:
    if value not in result:
        result[value] = 1
    else:
        result[value] += 1

for key, value in result.items():
    print(f"{key:.1f} - {value} times")