n = int(input())
composes = {}

for i in range(n):
    data = input().split("|")

    piece = data[0]
    composer = data[1]
    key = data[2]

    composes[piece] = {composer:key}

while True:
    data = input()
    if data == "Stop":
        break

    data = data.split("|")

    command = data[0]
    piece = data[1]

    if command == "Add":
        composer = data[2]
        key = data[3]
        if piece in composes:
            print(f"{piece} is already in the collection!")
        else:
            composes[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == "Remove":
        piece = data[1]

        if piece in composes:
            del composes[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif composes == "ChangeKey":
        piece = data[1]
        new_key = data[2]

        if piece in composes:
            composes[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, composer in composes.items():
    name = next(iter(composer))
    print(f"{piece} -> Composer: {name}, Key: {composer[name]}")