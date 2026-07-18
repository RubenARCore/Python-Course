key = input().split()


while True:
    data = input()
    if data == "find":
        break
        
    result = ""
    i = 0
    type_ = ""
    coordinates = ""

    for char in data:

        result += chr(ord(char) - int(key[i]))

        i += 1

        if i == len(key):
            i = 0

    type_start = result.find("&")
    type_end = result.rfind("&")

    coordinates_start = result.find("<")
    coordinates_end = result.rfind(">")

    type_ = result[type_start + 1:type_end]
    coordinates = result[coordinates_start + 1:coordinates_end]

    print(f"Found {type_} at {coordinates}")
