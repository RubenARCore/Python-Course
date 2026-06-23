data = list(map(str, input().split(" ")))

for i in range(len(data)):
    first_letter = list(data[i])
    digit = ""
    for letter in range(len(first_letter)):
        if first_letter[0].isdigit():
            digit += first_letter[0]
            first_letter.pop(0)
    first_letter[0], first_letter[-1] = first_letter[-1], first_letter[0]
    first_letter.insert(0, chr(int(digit)))
    data[i] ="".join(first_letter)

print(" ".join(data))