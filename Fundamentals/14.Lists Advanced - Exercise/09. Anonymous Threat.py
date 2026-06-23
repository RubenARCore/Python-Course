data = input().split()

command = input()

while command != "3:1":
    tokens = command.split()
    action = tokens[0]

    if action == "merge":
        start = int(tokens[1])
        end = int(tokens[2])

        if start < 0:
            start = 0
        if end >= len(data):
            end = len(data) - 1

        if start < len(data) and end >= 0 and start <= end:
            merged = "".join(data[start:end + 1])
            data = data[:start] + [merged] + data[end + 1:]

    elif action == "divide":
        index = int(tokens[1])
        partitions = int(tokens[2])

        element = data[index]
        part_len = len(element) // partitions
        extra = len(element) % partitions

        result = []
        start = 0

        for i in range(partitions):
            if i == partitions - 1:
                result.append(element[start:])
            else:
                result.append(element[start:start + part_len])
                start += part_len

        data = data[:index] + result + data[index + 1:]

    command = input()

print(" ".join(data))