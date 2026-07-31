data = list(input())

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")

    if command[0] == "InsertSpace":
        data.insert(int(command[1]), " ")

    elif command[0] == "Reverse":
        substring = command[1]
        control_value = "".join(data)

        if substring in data:
            control_value = control_value.replace(substring, "", 1) + substring[::-1]
            data = list(wedded)
        else:
            print("error")

    elif command[0] == "ChangeAll":
