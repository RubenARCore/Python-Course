input_data = input().split(" & ")

while True:
    command = input().split(" ")

    if command[0] == "Plant":
        if command[1] in input_data:
            continue
        else:
            input_data.insert(0, command[1])
    elif command[0] == "Transplant":
        if command[1] not in input_data:
            continue
        else:
            index_ = input_data.index(command[1])
            moved_item = input_data.pop(index_)
            input_data.append(moved_item)
            # input_data.append(input_data.pop(index_))
    elif command[0] == "Replace":
        if 0 <= int(command[1]) < len(input_data) and 0<= int(command[2]) < len(input_data):
            input_data[int(command[1])], input_data[int(command[2])] = input_data[int(command[2])], input_data[int(command[1])]
        else:
            continue
    elif command[0] == "Uproot":
        if command[1] not in input_data:
            continue
        else:
            index_ = input_data.index(command[1])
            input_data.pop(index_)
    elif command[0] == "Collect!":
        print(" | ".join(input_data))
        exit()