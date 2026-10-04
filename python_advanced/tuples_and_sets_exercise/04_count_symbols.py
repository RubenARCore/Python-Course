data = list(input())
data.sort()
result = {}

for item in data:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1
for key, value in result.items():
    print(f"{key}: {value} time/s")