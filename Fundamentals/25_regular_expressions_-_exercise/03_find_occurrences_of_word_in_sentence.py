import re

data = input().lower()
word = input().lower()

result = len(re.findall(rf"\b{word}\b", data))

print(result)