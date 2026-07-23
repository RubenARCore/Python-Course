import re

while True:
    data = input()
    if not data:
        break

    pattern = r'\d+'

    matches = re.findall(pattern, data)
    if len(matches) != 0:
        print(" ".join(matches), end=" ")

