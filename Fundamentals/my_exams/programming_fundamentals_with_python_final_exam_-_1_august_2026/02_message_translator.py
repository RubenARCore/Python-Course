import re

pattern = r"!([A-Z][a-z]{3,})!:\[([A-Z][A-Za-z]{8,})\]"

n = int(input())

for i in range(n):
    input_command = input()
    matches = re.findall(pattern, input_command)

    if matches:
        command = matches[0][0]
        match = matches[0][1]

        x = [ord(x) for x in match]
        x = [str(x) for x in x]
        print(f"{command}: {' '.join(x)}")

    else:
        print("The message is invalid")

