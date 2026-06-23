data = list(map(int, input().split()))
removed_sum = 0

while data:
    index = int(input())

    if index < 0:
        removed = data[0]
        data[0] = data[-1]
    elif index >= len(data):
        removed = data[-1]
        data[-1] = data[0]
    else:
        removed = data.pop(index)

    removed_sum += removed

    for i in range(len(data)):
        if data[i] <= removed:
            data[i] += removed
        else:
            data[i] -= removed

print(removed_sum)