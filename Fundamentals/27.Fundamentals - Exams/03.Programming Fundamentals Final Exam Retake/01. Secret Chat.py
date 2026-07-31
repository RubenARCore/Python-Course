data = list(input())

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")

    if command[0] == "InsertSpace":
        data.insert(int(command[1]), " ")
        print("".join(data))

    elif command[0] == "Reverse":
        substring = command[1]
        control_value = "".join(data)

        if substring in control_value:
            control_value = control_value.replace(substring, "", 1) + substring[::-1]
            print(control_value)
            data = list(control_value)
        else:
            print("error")

    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        control_value = "".join(data)
        control_value = control_value.replace(substring,replacement)
        print(control_value)
        data = list(control_value)

print(f"You have a new text message: {''.join(data)}")