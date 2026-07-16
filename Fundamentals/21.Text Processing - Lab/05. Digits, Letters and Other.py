data = input()
digits = []
letters = []
other_characters = []


for char in data:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        other_characters.append(char)

print("".join(digits))
print("".join(letters))
print("".join(other_characters))