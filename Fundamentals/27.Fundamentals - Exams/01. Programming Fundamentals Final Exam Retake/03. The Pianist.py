n = int(input())
composes = {}


for i in range(n):
    data = input().split("|")

    if data[1] not in composes:
        composes[data[1]] = {data[2]:[data[0]]}
    else:
        if data[2] in composes[data[1]]:
            composes[data[1]][data[2]].append(data[0])
        else:
            composes[data[1]][data[2]] = [data[0]]


while True:
    data = input()
    if data == "Stop":
        break

    data = data.split("|")

    if data[0] == "Add":
        if data[2] in composes:
            if data[3] in composes[data[2]]:
                print(f"{data[1]} is already in the collection!")
        else:
            composes[data[2]] = {data[3]: [data[1]]}
            print(f"{data[1]} by {data[2]} in {data[3]} added to the collection!")

    elif data[0] == "Remove":
        for composer in composes:
            for key in composes[composer]:
                for song in composes[composer][key]:
                    if song == data[1]:
                        print(f"Successfully removed {song}!")
                        composes[composer][key].remove(song)
                    else: #flag
                        print(f"Invalid operation! {song} does not exist in the collection.")


    elif data[0] == "ChangeKey":
        if data[1] in composes:
            print(data[1])
