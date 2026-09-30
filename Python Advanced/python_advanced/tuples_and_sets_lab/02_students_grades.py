n = int(input())
result = {}

for i in range(n):
    data = input().split()
    if data[0] not in result:
        result[data[0]] = [float(data[1])]
    else:
        result[data[0]].append(float(data[1]))

for key, values in result.items():
    print(f"{key} -> " , end="")
    for value in values:
        print(f"{value:.2f} ", end="")
    print(f"(avg: {sum(values) / len(values):.2f})")


