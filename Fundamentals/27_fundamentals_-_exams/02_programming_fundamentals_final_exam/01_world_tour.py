data = list(input())

while True:
    command = input().split(":")
    if command[0] == "Travel":
        break

    if command[0] == "Add Stop":
        index = int(command[1])
        data_string = list(command[2])

        if 0 <= index < len(data):
            for i in range(len(data_string)):
                data.insert(index + i, data_string[i])

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])

        if 0 <= start_index < len(data) and 0 <= end_index < len(data):
            for j in range( (end_index - start_index) +1 ):
                data.pop(start_index)

    elif command[0] == "Switch":
        old_string = command[1]
        new_String = command[2]
        control_string = "".join(data)
        control_string = control_string.replace(old_string, new_String)
        data = list(control_string)

    print("".join(data))

print(f"Ready for world tour! Planned stops: {''.join(data)}")

