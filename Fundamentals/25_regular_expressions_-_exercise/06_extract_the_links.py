import re
pattern = r'(www)\.([A-Za-z0-9-]+)(?:\.[a-z]+)+'

while True:
    data = input()
    if not data:
        break

    matches = re.search(pattern, data)

    if matches:
        print(matches.group(0))