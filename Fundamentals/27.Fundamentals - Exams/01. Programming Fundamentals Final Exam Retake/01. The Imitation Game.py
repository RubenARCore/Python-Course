message = list(input())

while True:
    data = input()
    if data == "Decode":
        break

    data = data.split("|")

    if data[0] == "Move":
        moved_index = message[:int(data[1])]
        message = message.__add__(moved_index)
        for i in range(int(data[1])):
            message.pop(0)

    elif data[0] == "Insert":

        message[int(data[1]):int(data[1])] = list(data[2])

    elif data[0] == "ChangeAll":

        for char in message:
            if char == data[1]:
                message[message.index(char)] = data[2]

print("The decrypted message is: "+"".join(message))