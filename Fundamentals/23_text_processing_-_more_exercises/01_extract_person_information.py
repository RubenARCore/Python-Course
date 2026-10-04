n = int(input())

for _ in range(n):
    
    data = input()

    name = ""
    age = ""

    for i in range(len(data)):
        if data[i] == "@":
            i += 1
            while i < len(data) and data[i] != "|":
                name += data[i]
                i += 1

        if data[i] == "#":
            i += 1
            while i < len(data) and data[i] != "*":
                age += data[i]
                i += 1

    print(f"{name} is {age} years old.")