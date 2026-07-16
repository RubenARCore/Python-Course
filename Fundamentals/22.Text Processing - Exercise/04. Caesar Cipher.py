data = input()

for char in data:

    char_to_number = ord(char) + 3
    print(chr(char_to_number), end='')