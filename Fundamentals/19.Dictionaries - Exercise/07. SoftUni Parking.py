n = int(input())
registered = {}

for i in range(n):
    data = input().split()



    if len(data) == 3:
        command, name, plate_number = data
    else:
        command, name = data
        plate_number = "registered[name]"


    if command == "register":
        if name not in registered:
            registered[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    else:
        if data[1] not in registered:
            print(f"ERROR: user {name} not found")
            
        else:
            print(f"{name} unregistered successfully")
            registered.pop(name)

for name, plate_number in registered.items():
    print(f"{name} => {plate_number}")