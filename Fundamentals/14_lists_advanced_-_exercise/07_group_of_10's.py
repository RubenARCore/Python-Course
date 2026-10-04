data = list(map(int, input().split(", ")))
result = []
start_point = 0

if data[-1] % 10 == 0:
    range_ = (data[-1] // 10) + 1
else:
    range_ = (data[-1] // 10) + 2

for i in range(1, range_):

    end_point = i * 10
    current = [x for x in data if start_point < x <= end_point]
    start_point, end_point = end_point, start_point
    result.append(current)

for i in range(len(result)):
    print(f"Group of {(i+1)*10}\'s: {result[i]}")
