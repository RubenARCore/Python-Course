data = input().replace(" ", "")
data = list(data)

char_in_string = {}

for char in data:
    if char not in char_in_string:
        char_in_string[char] = 1
    else:
        char_in_string[char] += 1

for key, value in char_in_string.items():
    print(f"{key} -> {value}")