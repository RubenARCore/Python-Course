input_data = input()

data = []

while input_data != "End":
    data.append(input_data.split("-"))
    data[-1][0] = int(data[-1][0])

    input_data = input()

data.sort()

result = [n.pop(1) for n in data]

print(result)