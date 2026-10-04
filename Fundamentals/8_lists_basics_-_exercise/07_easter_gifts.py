gifts = input().split(" ")
command = input().split(" ")

while command[0] != "No":


    if command[0] == "OutOfStock":
        while command[1] in gifts:
            gifts[gifts.index(command[1])] = "None"

    elif command[0] == "Required":
        if 0 < int(command[2]) < len(gifts):
            gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[len(gifts)-1] = command[1]

    command = input().split(" ")

while "None" in gifts:

    gifts.remove("None")

print(" ".join(gifts))

