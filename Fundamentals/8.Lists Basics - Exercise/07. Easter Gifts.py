gifts = input().split(" ")
command = None

while command != "No Money":

    command = input().split(" ")

    if command[0] == "OutOfStock":
       index_none = gifts.index(command[1])
       gifts[index_none] = "None"

    elif command[0] == "Required":
        pass
    elif command[0] == "JustInCase":
        pass



