data = list(input())

while ":" in data:
    index = data.index(':')

    print(data[index]+data[index + 1])
    data.pop(index)
