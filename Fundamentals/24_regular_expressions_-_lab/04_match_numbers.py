import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

data = input()

matches = re.finditer(pattern, data)

for match in matches:
    print(match.group(), end=" ")