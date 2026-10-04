input_data = input().split(", ")
n = int(input())

for i in range(n):
    command = input().split(", ")

    if command[0] == "Add":
        if command[1] in input_data:
            print("Card is already in the deck")
        else:
            input_data.append(command[1])
            print("Card successfully added")

    elif command[0] == "Remove":
        if command[1] not in input_data:
            print("Card not found")
        else:
            input_data.remove(command[1])
            print("Card successfully removed")

    elif command[0] == "Remove At":
        index = int(command[1])
        if not 0 <= index < len(input_data):
            print("Index out of range")
        else:
            input_data.pop(index)
            print("Card successfully removed")

    elif command[0] == "Insert":
        index = int(command[1])

        if not 0 <= index <= len(input_data):
            print("Index out of range")
        elif command[2] in input_data:
            print("Card is already added")
        else:
            input_data.insert(index, command[2])
            print("Card successfully added")

print(", ".join(input_data))