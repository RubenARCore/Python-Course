n = int(input())
registered = {}

for i in range(n):
    data = input().split()

    command, name, plate_number = data

    if command == "register":
        if name not in registered:
            registered[name] = plate_number
            print(f"{name} registered {plate_number}")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    else:
        registered.pop(name)