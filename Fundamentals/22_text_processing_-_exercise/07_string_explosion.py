data = input()

result = ""
strength = 0

for i in range(len(data)):
    if data[i] == ">":
        result += ">"
        strength += int(data[i + 1])
    else:
        if strength > 0:
            strength -= 1
        else:
            result += data[i]

print(result)