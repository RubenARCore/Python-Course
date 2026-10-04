import re

data = input()
pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"
points = 0
matches = re.findall(pattern, data)
result = []

for item in matches:
    points += len(item[1])
    result.append(item[1])


print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {points}")