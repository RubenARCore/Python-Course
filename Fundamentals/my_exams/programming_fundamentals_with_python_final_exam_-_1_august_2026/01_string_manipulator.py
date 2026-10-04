data = input()

while True:
    command = input()
    if command == "End":
        break
    command = command.split()

    if command[0] == "Translate":
        char = command[1]
        replacement = command[2]
        data = data.replace(char, replacement)
        print(data)
    elif command[0] == "Includes":
        substring = command[1]
        x = data.find(substring)
        if x == -1:
            print("False")
        else:
            print("True")
    elif command[0] == "Start":
        substring = command[1]
        x = data.startswith(substring)
        print(x)
    elif command[0] == "Lowercase":
        data = data.lower()
        print(data)
    elif command[0] == "FindIndex":
        char = command[1]
        x = data.rfind(char)
        print(x)
    elif command[0] == "Remove":
        start_index = int(command[1])
        count = int(command[2])
        data = list(data)
        del data[start_index:start_index + count]
        data = "".join(data)
        print(data)